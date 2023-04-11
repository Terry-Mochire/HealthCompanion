import json
from datetime import datetime, timedelta

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from booking.models import FirebaseUser, Appointment
from clinic.models import Clinic


def save_user(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)

        user = FirebaseUser()
        user.user_id = data_dict.get("user_id")
        user.email = data_dict.get("email")
        user.name = data_dict.get("name")
        if FirebaseUser.objects.filter(uid=user.user_id).count() < 1:
            user.save()
            return HttpResponse("User saved successfully")
        else:
            return HttpResponse("User already exists")
    else:
        return HttpResponse("Invalid request")


def get_user(request, user_id):
    print(user_id)
    user = FirebaseUser.objects.get(uid=user_id)
    print(user)
    data = serialize('json', [user])
    return HttpResponse(data, content_type="application/json")


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def booking(request):
    weekdays = validWeekday(21)
    validatedWeekdays = isWeekdayValid(weekdays)
    response_data = {
        'dates': validatedWeekdays
    }

    json_response = json.dumps(response_data)

    if request.method == "POST":
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)

        user_id = data_dict.get("user_id")
        print(user_id)
        service = data_dict.get("service")
        clinic = data_dict.get("clinic")
        day = data_dict.get("day")

        if not service:
            return HttpResponse("Please select a service")

        if not clinic:
            return HttpResponse("Please select a clinic")

        if not day:
            return HttpResponse("Please select a day")

        request.session['service'] = service
        request.session['clinic'] = clinic
        request.session['day'] = day

        return redirect("booking_submit/{}".format(user_id))

    return HttpResponse(json_response, content_type="application/json")


def booking_submit(request, user_id):
    user = FirebaseUser.objects.get(uid=user_id)
    print(user)
    service = request.session.get('service')
    print(service)
    clinic = request.session.get('clinic')
    returnedClinic = Clinic.objects.get(name=clinic)
    print(clinic)
    day = request.session.get('day')
    print(day)

    times = [
        "8AM", "8:30AM", "9AM", "9:30AM", "10AM", "10:30AM", "11AM", "11:30AM", "12PM", "12:30PM", "1PM", "1:30PM",
        "2PM", "2:30PM", "3PM", "3:30PM", "4PM", "4:30PM", "5PM", "5:30PM", "6PM", "6:30PM", "7PM", "7:30PM", "8PM",
        "8:30PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    hours = checkTime(times, day)
    response_data = {
        'hours': hours
    }

    json_response = json.dumps(response_data)

    if request.method == "POST":
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)

        time = data_dict.get("time")
        print(time)
        date = dayToWeekday(day)

        if service != None and returnedClinic != None:
            if maxDate >= day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            appointment = Appointment()
                            appointment.user = user
                            appointment.service = service
                            appointment.clinic = returnedClinic
                            appointment.day = day
                            appointment.time = time
                            appointment.save()
                            return JsonResponse({"message": "Appointment booked successfully"})
                        else:
                            return JsonResponse({"message": "Selected time is not available"})
                    else:
                        return JsonResponse({"message": "Selected day is not available"})
                else:
                    return JsonResponse({"message": "Selected day is not a weekday"})
            else:
                return JsonResponse({"message": "Selected day is not valid"})
        else:
            return JsonResponse({"message": "Please select a service and a clinic"})

    return HttpResponse(json_response, content_type="application/json")


def get_appointments(request, user_id):
    user = FirebaseUser.objects.get(uid=user_id)
    appointments = Appointment.objects.filter(user=user)
    data = serialize('json', appointments)
    return HttpResponse(data, content_type="application/json")


def get_appointments_by_clinic(request, clinic):
    appointments = Appointment.objects.filter(clinic=clinic)
    data = serialize('json', appointments)
    return HttpResponse(data, content_type="application/json")
