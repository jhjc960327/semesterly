"""This file contains all dicts which map a school to its associated object"""
from uoft_parser import UofTParser
from hopkins_parser import HopkinsParser
from umd_parser import UMDParser
from timetable.models import *

school_to_models = {
    'jhu': (HopkinsCourse, HopkinsCourseOffering),
    'uoft': (Course, CourseOffering),
    'umd': (UmdCourse, UmdCourseOffering),
    'rutgers': (RutgersCourse, RutgersCourseOffering),
    'uo': (OttawaCourse, OttawaCourseOffering)
}

school_to_parser = {
	'jhu': HopkinsParser,
    'uoft': UofTParser,
    'umd': UMDParser,
    'rutgers': None,
    'uo': None
}

# the smallest number of minutes needed to describe start/end times
# e.g. uoft classes only start on the hour or half hour, so granularity is 30min
school_to_granularity = {
    'jhu': 5,
    'uoft': 30,
    'umd': 5,
    'rutgers': 5
}