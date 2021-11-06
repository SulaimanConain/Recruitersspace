
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask.helpers import make_response
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import TelField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Email, Length
from models import Canidates, RegistrationControls
from models import db
from flask_csv import send_csv
from collections import defaultdict
from hardcoded_data import departments_choices, domains_choices, year_choices, departments, year
import json
main = Blueprint('main', __name__)


def counters():
    return defaultdict(int)


def freqs(data):
    r = defaultdict(counters)
    for d in data:
        for k, v in d.items():
            r[k][v] += 1
    return dict(((k, dict(v))) for k, v in r.items())


class RegistrationsForm(FlaskForm):
    first_name = StringField(
        'first_name', validators=[DataRequired('First Name cannot be empty')])
    last_name = StringField('last_name', validators=[
                            DataRequired('Last Name cannot be empty')])
    email = StringField('email', validators=[DataRequired(
        'Email cannot be empty'), Email('Email is badly formated')])
    phone = TelField('phone', validators=[
                     DataRequired('Phone cannot be empty'), Length(min=11, max=11, message='Phone number is not correct')])
    department = SelectField('department', choices=departments_choices, validators=[
                             DataRequired('Department cannot be empty')])
    year = SelectField('year', choices=year_choices, validators=[
                       DataRequired('Year cannot be empty')])
    pastexp = TextAreaField('pastexp', [DataRequired(
        'Past Experience cannot be empty'), Length(max=500)])
    domain = SelectField('domain', choices=domains_choices, validators=[
                         DataRequired('Domain cannot be empty')])
    reason = TextAreaField('reason', [DataRequired(
        'Reason cannot be empty'), Length(max=700)])


@main.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationsForm()
    if form.validate_on_submit() and RegistrationControls.query.one().isRegistration:
        try:
            canidate = Canidates(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, past_experience=form.pastexp.data, reason=form.reason.data,
                                 phone_number=form.phone.data, department=form.department.data, year=form.year.data, domain=form.domain.data, status="pending", remarks='none', remarks_by='none')

            db.session.add(canidate)
            db.session.commit()
            flash(
                'Registartions Succesful check your email for further announcements.', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash('Email already exists.', 'danger')
            return redirect(url_for('main.index'))

    return render_template('index.html', form=form, query=RegistrationControls.query.one())


@main.route('/registrations', methods=['GET', 'POST'])
@login_required
def registrations():
    if request.method == 'GET':
        try:
            return render_template('registrations.html', query=Canidates.query.all(), departments=departments, year=year)
        except:
            return render_template('registrations.html', query=[])
    else:
        return redirect(url_for('auth.login'))


@main.route('/viewdetails', methods=['GET'])
@login_required
def view_details():
    email = request.args.get('email')
    if RegistrationControls.query.one().isRegistration:
        try:
            return render_template('viewdetails.html', query=Canidates.query.filter_by(email=email))
        except:
            return redirect(url_for('main.registrations'))
    else:
        return redirect(url_for('auth.login'))


@main.route('/viewdetails', methods=['POST'])
@login_required
def interviwe_selection():
    if RegistrationControls.query.one().isRegistration:
        selection = request.form.get('interviewee_select')
        remarks = request.form.get('remarks')
        if selection != "" and remarks != "":
            email = request.args.get('email')
            try:
                current = Canidates.query.filter_by(email=email).first()
                current.remarks = remarks
                current.status = selection
                current.remarks_by = current_user.name
                db.session.commit()
                return render_template('viewdetails.html', query=Canidates.query.filter_by(email=email))
            except:
                return redirect(url_for('main.registrations'))
    else:
        return redirect(url_for('auth.login'))


@main.route('/filterby', methods=['POST'])
@login_required
def filter_by():
    filterbyarg = request.form.get('filterby')
    filterfollowing = request.form.get('filterfollowing')
    if(filterbyarg == 'department'):
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(department=filterfollowing))
        except:
            return render_template('registrations.html', query=Canidates.query.all())
    if(filterbyarg == 'all'):
        try:
            return render_template('registrations.html', query=Canidates.query.all())
        except:
            return render_template('registrations.html', query=Canidates.query.all())
    if(filterbyarg == 'status'):
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(status=filterfollowing))
        except:
            return render_template('registrations.html', query=Canidates.query.all())
    else:
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(year=filterfollowing))
        except:
            return render_template('registrations.html', query=Canidates.query.all())


@main.route('/searchby', methods=["POST"])
@login_required
def search_by():
    searchbytype = request.form.get('searchbylist')
    searchbyvalue = request.form.get('searchby')
    if(searchbytype == 'first_name'):
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(first_name=searchbyvalue))
        except:
            return render_template('registrations.html', query=Canidates.query.all())
    if(searchbytype == 'phone_number'):
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(phone_number=searchbyvalue))
        except:
            return render_template('registrations.html', query=Canidates.query.all())
    if(searchbytype == 'email'):
        try:
            return render_template('registrations.html', query=Canidates.query.filter_by(email=searchbyvalue))
        except:
            return render_template('registrations.html', query=Canidates.query.all())


@main.route('/president_controls', methods=['POST'])
@login_required
def president_controls():
    if request.form['submit_button'] == 'Generate Records' and current_user.email == 'president@sentec.com':
        rows = Canidates.query.all()
        to_csv = []
        for i in rows:
            to_csv.append({
                'id': i.id,
                'first_name': i.first_name,
                          'last_name': i.last_name,
                          'email': i.email,
                          'past_experience': i.past_experience,
                          'reason': i.reason,
                          'phone_number': i.phone_number,
                          'departmnet': i.department,
                          'year': i.year,
                          'domain': i.domain,
                          'status': i.status,
                          'remarks': i.remarks,
                          'remarks_by': i.remarks_by,
                          })
        return send_csv(to_csv, 'DetailedReport.csv', ["id",
                                                       "first_name",
                                                       "last_name",
                                                       "email",
                                                       "past_experience",
                                                       "reason",
                                                       "phone_number",
                                                       "departmnet",
                                                       "year",
                                                       "domain",
                                                       "status",
                                                       "remarks",
                                                       "remarks_by"])
    elif request.form['submit_button'] == 'Open Registrations' and current_user.email == 'president@sentec.com':
        registration_control = RegistrationControls.query.one()
        registration_control.isRegistration = True
        db.session.commit()
        flash('Registration Open', category='success')
        return render_template('registrations.html', query=Canidates.query.all(), departments=departments, year=year)

    else:
        registration_control = RegistrationControls.query.one()
        registration_control.isRegistration = False
        db.session.commit()
        flash('Registration Closed', category='danger')
        return render_template('registrations.html', query=Canidates.query.all(), departments=departments, year=year)


@main.route('/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    if request.method == 'GET' and RegistrationControls.query.one().isRegistration:
        try:
            data = [dict(u) for u in Canidates.query.with_entities(
                Canidates.department, Canidates.domain, Canidates.year, Canidates.status)]
            data_stats = freqs(data)
            return render_template('statistics.html', department=data_stats['department'].items(), domain=data_stats['domain'].items(), year=data_stats['year'].items(), status=data_stats['status'].items(), departmentJSON=str(json.dumps({k: v for (k, v) in data_stats['department'].items()})), domainJSON=str(json.dumps({k: v for (k, v) in data_stats['domain'].items()})), yearJSON=str(json.dumps({k: v for (k, v) in data_stats['year'].items()})), statusJSON=str(json.dumps({k: v for (k, v) in data_stats['status'].items()})))
        except Exception as e:
            print(e)
            return render_template('statistics.html')
    else:
        return redirect(url_for('auth.login'))


@main.route('/delete', methods=['POST'])
@login_required
def delete():
    if current_user.email == 'president@sentec.com':
        email = request.form.get('email')
        current_canidate = Canidates.query.filter_by(email=email).first()
        db.session.delete(current_canidate)
        db.session.commit()
        flash(f'Candidate {email} deleted ', category='danger')
        return redirect(url_for('main.registrations'))
    else:
        return redirect(url_for('auth.login'))
