from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .xml_utils import parse_xml_request, xml_response
import xml.etree.ElementTree as ET


@csrf_exempt
def create_student(request):

    if request.method != "POST":
        return xml_response({"error": "Only POST allowed"}, 405)

    data = parse_xml_request(request.body)

    if not data:
        return xml_response({"error": "Invalid XML"}, 400)

    student = Student.objects.create(
        name=data.get("name"),
        email=data.get("email"),
        age=data.get("age")
    )

    return xml_response({
        "message": "Student created",
        "id": student.id
    })


def get_students(request):

    students = Student.objects.all()

    root = ET.Element("students")

    for s in students:

        student = ET.SubElement(root, "student")

        ET.SubElement(student, "id").text = str(s.id)
        ET.SubElement(student, "name").text = s.name
        ET.SubElement(student, "email").text = s.email
        ET.SubElement(student, "age").text = str(s.age)

    xml = ET.tostring(root)

    return xml_response({}, root_tag="students")


def get_student(request, id):

    try:

        s = Student.objects.get(id=id)

        return xml_response({

            "id": s.id,
            "name": s.name,
            "email": s.email,
            "age": s.age

        }, root_tag="student")

    except Student.DoesNotExist:

        return xml_response({"error": "Student not found"}, 404)


@csrf_exempt
def update_student(request, id):

    if request.method != "PUT":
        return xml_response({"error": "Only PUT allowed"}, 405)

    try:

        student = Student.objects.get(id=id)

    except Student.DoesNotExist:

        return xml_response({"error": "Student not found"}, 404)

    data = parse_xml_request(request.body)

    student.name = data.get("name")
    student.email = data.get("email")
    student.age = data.get("age")

    student.save()

    return xml_response({"message": "Student updated"})


@csrf_exempt
def delete_student(request, id):

    if request.method != "DELETE":
        return xml_response({"error": "Only DELETE allowed"}, 405)

    try:

        student = Student.objects.get(id=id)

        student.delete()

        return xml_response({"message": "Student deleted"})

    except Student.DoesNotExist:

        return xml_response({"error": "Student not found"}, 404)