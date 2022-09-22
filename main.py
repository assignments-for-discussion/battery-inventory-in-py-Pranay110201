
def count_batteries_by_usage(cycles):
#   Variables to keep count of various categories of batteries
  lowcount=0
  mediumcount=0
  highcount=0
#   loop to iterate through the input values present in cycles
  for cycle in cycles:
#     condition to check and categorize them based of the cycles 
    if(cycle<410):
      lowcount+=1
    elif(cycle>=410 and cycle<909):
      mediumcount+=1
    else:
      highcount+=1
#    returning the count of each catergories of the batteries.
  return {
    "lowCount": lowcount,
    "mediumCount": mediumcount,
    "highCount": highcount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
#   boundry test cases
  counts = count_batteries_by_usage([410, 300, 909, 600, 900, 910])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
#   accepting inputs from the user
#   counts = count_batteries_by_usage(take_inputs())
#   assert((counts["lowCount"]+counts["mediumCount"]+counts["highCount"])==len(take_inputs))
  
def take_inputs():
    n=int(input("Enter the number of batteries"))
    cycles=[]
    print("Enter the cycles")
    for cycle in range(0,n):
        cycles.append(int(input()))
    return cycles


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
