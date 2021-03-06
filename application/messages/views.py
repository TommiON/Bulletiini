from application import app, db, login_required, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from datetime import datetime
from sqlalchemy.sql import text

from application.messages.models import Message
from application.messages.forms import MessageForm

# tulostaa luettelon kaikista viesteistä
@app.route("/messages", methods=["GET"])
def messages_list():
    return render_template("message_list.html", messages = Message.query.all())


# yksittäisen viestin tarkemmat tiedot
@app.route("/messages/<message_id>", methods=["GET"])
def message_details(message_id):
    message = Message.query.get(message_id)
    return render_template("message_details.html", message=message)


# poistaa yksittäisen viestin, sallittu vain viestin kirjoittaneelle tai adminille
@app.route("/messages/delete/<message_id>", methods=["GET"])
@login_required(role="BASIC")
def messages_delete(message_id):
    message_to_be_deleted = Message.query.get(message_id)
    
    # tarkistetaan onko kirjautunut käyttäjä viestin omistaja tai admin
    if (message_to_be_deleted.author_id != current_user.id and current_user.is_admin == False):
        return login_manager.unauthorized()
    
    # tallennetaan viestin thread_id palautus-urlia tai ketjun tuhoamista varten
    thread_id = message_to_be_deleted.thread_id
    
    # tuhotaan viesti
    db.session.delete(message_to_be_deleted)
    db.session.commit()

    # palataan keskusteluketjun näkymään tai poistetaan ketju jos poistettu viesti oli sen viimeinen
    messages_left = Message.messages_left_in_thread(thread_id)
    if messages_left == 0:
        return redirect(url_for("threads_delete", thread_id=thread_id))
    return redirect(url_for("thread_details", thread_id = thread_id))


# palauttaa esitäytetyn lomakkeen viestin editoimiseen
@app.route("/messages/edit/<message_id>", methods=["GET"])
@login_required(role="BASIC")
def messages_edit_form(message_id):
    message_to_be_edited = Message.query.get(message_id)
    form = MessageForm()
    form.title.data = message_to_be_edited.title
    form.content.data = message_to_be_edited.content
    return render_template("message_editing_form.html", form=form, message_id=message_id)


# korvaa viestin uudella (editointitoiminnallisuus), sallittu vain viestin kirjoittaneelle tai adminille
@app.route("/messages/edit/<message_id>", methods=["POST"])
@login_required(role="BASIC")
def messages_edit(message_id):
    message = Message.query.get(message_id)
    
    # tarkistetaan onko kirjautunut käyttäjä viestin omistaja tai admin
    if (message.author_id != current_user.id and current_user.is_admin == False):
        return login_manager.unauthorized()
    
    # haetaan lomakedata
    form = MessageForm(request.form)
    
    # tallennetaan viestin thread_id palautus-urlia varten
    thread_id = message.thread_id

    # validoidaan
    if not form.validate():
        return render_template("message_editing_form.html", form=MessageForm(), message_id=message_id)
    
    # päivitetään viesti
    message.title = form.title.data
    message.content = form.content.data
    db.session.commit()

    # palataan keskusteluketjun näkymään
    return redirect(url_for("thread_details", thread_id = thread_id))