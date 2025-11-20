import sys 
    #check if correct number og argumnets 
if len(sys.argv) != 3:
  print("Usage:python studnet.py<name><rollno>")
  sys.exit(1)
  #sys.argv[0] is always the prgram name
  script_name=sys.argv[0]
  name=sys.argv[1]
  rollno=sys.argv[2]
  #printing statements
  print("script Name:",script_name)
  print("script student name:",name)
  print("RollNumber:",rollno)
