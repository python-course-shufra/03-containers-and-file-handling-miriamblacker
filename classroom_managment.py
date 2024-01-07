classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]
def find_student(name):
    for k, val in enumerate(classroom):
        if val['name']==name:
            return k
    return -1

def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    pass
    if email is None:
        email=name+'@example.com'
    email=email.lower()
    new_student={
        'name': name,
        'email': email,
        'grades':[]
    }
    classroom.append(new_student)


def delete_student(name):
    """Delete a student from the classroom"""
    pass
    if find_student(name)!=-1:
        del classroom[find_student(name)]
    


def set_email(name, email):
    """Sets the email of the student"""
    pass
    i=find_student(name)
    if i!=-1:
        classroom[i]['email']=email


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    pass
    i=find_student(name)
    if i!= -1:
        classroom[i]['grades'].append((profession, grade))


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    pass
    i=find_student(name)
    avg=0
    cnt=0
    for j in classroom[i]['grades']:
        if j[0]==profession:
            avg+=j[1]
            cnt+=1
    return avg/cnt


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    pass
    prof=[]
    i=find_student(name)
    for j in  classroom[i]['grades']:
        if j[0] not in prof:
            prof.append(j[0])
    return prof
