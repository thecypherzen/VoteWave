#!/usr/bin/python3

from models import storage
from models.options import Option
from sys import exit


print("+++++++++++[Fetching Question]++++++++++++")
questions = storage.all("Question")

if not questions:
    print("No question found.")
    exit(1)

for question in questions:
    if not question.options:
        break

if not question:
    question = questions[-1]

print(f"\tFound: Question {question.serial}({question.id})")

qopts_len_b4 = len(question.options)


print("+++++++++++[Creating 1 Options]++++++++++++")
opt = Option(question_id=question.id, value=f"option-{qopts_len_b4+1}")
if not opt:
    print("\Failure -> couldn't create option")
    exit(1)
opt.save()
print(f"\t Success -> {opt.id}")

print("+++++++++++[Check Details]++++++++++++")
print("\toption is in storage and question is owner -> {}".format(
    all([(op := storage.get("Option", opt.id)) is not None,
         op.question_id == question.id])))
print("\toption in question's options -> {}".format(
    all([opt in question.options, qopts_len_b4 ==
         len(question.options) - 1])))
print("\toption.question works -> {}".format(
    all([opt.question is not None, opt.question is question])))
