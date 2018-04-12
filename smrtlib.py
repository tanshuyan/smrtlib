# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:21:48 2018

@author: shuyan

smrtlib
"""

#This is a standard library of useful functions
#Required files: Lookup Table.xlsx

import sys, os
import pandas as pd

_emu_to_vobc_dict = None
_vobc_to_emu_dict = None
_emu_to_emu2_dict = None
_vobc_to_emu2_dict = None
_emu_to_type_dict = None
_emu_to_name_dict = None
_train_id_to_emu_dict = None
_emu_to_train_id_dict = None

#Excel file headers
_type_header = 'Type'
_name_header = 'Name'
_emu_header = 'EMU'
_emu2_header = 'EMU2'
_vobc_header = 'VOBC ID'
_train_id_header = 'Train ID'


#Returns a dataframe containing the trains lookup table
def _get_train_lookup_df():
    #Get path to train lookup table
    tableDir = os.getcwd()
    tableDir = os.path.join(tableDir, 'Lookup Table.xlsx')
    #Extract all train info into a dataframe
    train_df = pd.read_excel(open(tableDir,'rb'), sheet_name='Trains')
    return train_df

#Converts EMU/DT id to VOBC ID
#e.g. 3001 -> 1001
def emu_to_vobc(emu_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _emu_to_vobc_dict
    if _emu_to_vobc_dict is None:
        _emu_to_vobc_dict = _get_train_lookup_df().set_index(_emu_header)[_vobc_header].to_dict()
        print ("emu_to_vobc dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        emu_number = int(emu_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _emu_to_vobc_dict.get(emu_number, "")

#Converts VOBC ID to EMU/DT id
#e.g. 1001 -> 3001
def vobc_to_emu(vobc_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _vobc_to_emu_dict
    if _vobc_to_emu_dict is None:
        _vobc_to_emu_dict = _get_train_lookup_df().set_index(_vobc_header)[_emu_header].to_dict()
        print ("vobc_to_emu dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        vobc_number = int(vobc_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _vobc_to_emu_dict.get(vobc_number, "")

#Converts EMU/DT id to EMU2 format
#e.g. 3001 -> 3001/3002
def emu_to_emu2(emu_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _emu_to_emu2_dict
    if _emu_to_emu2_dict is None:
        _emu_to_emu2_dict = _get_train_lookup_df().set_index(_emu_header)[_emu2_header].to_dict()
        print ("emu_to_emu2 dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        emu_number = int(emu_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _emu_to_emu2_dict.get(emu_number, "")

#Converts VOBC id to EMU2 format
#e.g. 1001 -> 3001/3002
def vobc_to_emu2(vobc_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _vobc_to_emu2_dict
    if _vobc_to_emu2_dict is None:
        _vobc_to_emu2_dict = _get_train_lookup_df().set_index(_vobc_header)[_emu2_header].to_dict()
        print ("vobc_to_emu2 dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        vobc_number = int(vobc_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _vobc_to_emu2_dict.get(vobc_number, "")

#Converts EMU/DT id to train type
#e.g. 3001 -> KHI
def emu_to_type(emu_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _emu_to_type_dict
    if _emu_to_type_dict is None:
        _emu_to_type_dict = _get_train_lookup_df().set_index(_emu_header)[_type_header].to_dict()
        print ("emu_to_type dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        emu_number = int(emu_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _emu_to_type_dict.get(emu_number, "")

#Converts EMU/DT id to train name
#e.g. 3001 -> KHI32
def emu_to_name(emu_number):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _emu_to_name_dict
    if _emu_to_name_dict is None:
        _emu_to_name_dict = _get_train_lookup_df().set_index(_emu_header)[_name_header].to_dict()
        print ("emu_to_name dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        emu_number = int(emu_number)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _emu_to_name_dict.get(emu_number, "")

#Converts train id to EMU/DT id
#e.g. 1 -> 3001
def train_id_to_emu(train_id):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _train_id_to_emu_dict
    if _train_id_to_emu_dict is None:
        _train_id_to_emu_dict = _get_train_lookup_df().set_index(_train_id_header)[_emu_header].to_dict()
        print ("_train_id_to_emu_dict dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        train_id = int(train_id)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _train_id_to_emu_dict.get(train_id, "")

#Converts EMU/DT id to train id
#e.g. 3001 -> 1
def emu_to_train_id(emu_id):
    #initialise the lookup dictionary if it has not already been initialised.
    #This means that the program only has to read the lookup table excel file once, and not for every subsequent call of this function 
    #Very speed
    global _emu_to_train_id_dict
    if _emu_to_train_id_dict is None:
        _emu_to_train_id_dict = _get_train_lookup_df().set_index(_emu_header)[_train_id_header].to_dict()
        print ("_EMU_to_train_id_dict dictionary initialised")
    #If the input was given in string format, convert it to an integer
    try:
        emu_id = int(emu_id)
    except ValueError:
        pass
    #Returns the corresponding vobc number, but returns an empty string if the emu number entry cannot be found
    return _emu_to_train_id_dict.get(emu_id, "")

#Checks whether an indicated time "now" is between a start time and an end time.
#Input: now, start, end times, all as python Time objects
#Output: Boolean True/False
def time_is_in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end