import pytest
import io
import os
from user_functions import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'
    
def test_username_with_input_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO("\n"))
    assert get_user_name_from_input() is None
    

def test_username_with_input_having_empty_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('adri e'))
    assert get_user_name_from_input() is None
    

def test_username_with_correct_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('adrien'))
    assert get_user_name_from_input()=='adrien'
    

def test_username_with_unstrip_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' adrien  '))
    assert get_user_name_from_input()=='adrien'
    
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """

def test_pwd_bad_size_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a'))
    assert get_password_from_input() is None
     

def test_pwd_none_number_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('abcdefgha%'))
    assert get_password_from_input() is None

    
def test_pwd_none_spec_char_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('abcdefgha8'))
    assert get_password_from_input() is None
    

def test_pwd_none_letter_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12345678%'))
    assert get_password_from_input() is None

def test_pwd_good_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('A12345678%'))
    assert get_password_from_input()=='A12345678%'

def test_is_palindrome_input_palindrom(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('La mariée ira mal'))
    assert is_palindrome() is True

def test_is_palindrome_input_not_palindrom(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Le marié ira mal'))
    assert is_palindrome() is False