# Sean Bucholtz
# CSC 110 Section 3
# 5/24/13
# Assignment #6

# Greeting
print('Welcome to Voter View: A voter data analyzer')

# Open
filename = input('\n\nSpecify the data file that you would like to analyze: ')
data_file = open(filename, 'r')
dataout = open('REPORT-' + filename, 'w')

# creates one list of all data
def get_list():
    nums_1 = []
    line = data_file.readline()
    while line != '':
        number = float(line.rstrip())
        nums_1.append(number)
        line = data_file.readline()
    return nums_1

# creates individual lists for the specific value groups
def gen_lists(nums_1):
    
    year_list_1 = [] 
    eligible_voter_list_1 = [] 
    registered_voter_list_1 = [] 
    num_ballots_cast_1 = []

    for num in range(0,len(nums_1),4):
        year_list_1.append(int(nums_1[num]))

    for num in range(1,len(nums_1),4):
        eligible_voter_list_1.append(int(nums_1[num]))

    for num in range(2,len(nums_1),4):
        registered_voter_list_1.append(int(nums_1[num]))
        
    for num in range(3,len(nums_1),4):
        num_ballots_cast_1.append(int(nums_1[num]))

    return year_list_1, eligible_voter_list_1, registered_voter_list_1, \
           num_ballots_cast_1

# Generates value ratios and creates a user report doc
def create_report(r_year_list,r_eligible_voter_list,\
                  r_registered_voter_list,r_num_ballots_cast ):
    r_percent_list = [] # registered:eligible
    r_voted_list = [] # votes:registered

    # Generates a lists of percents for each year
    for num in range(len(r_year_list)):
        #index values are used to keep keep the group values aligned
        percent = ((r_registered_voter_list[num]))/\
                   (r_eligible_voter_list[num])*100
        voted = ((r_num_ballots_cast[num])/\
                 (r_registered_voter_list[num]))*100
        r_percent_list.append(percent)
        r_voted_list.append(voted)
        dataout.write('In ' + str(r_year_list[num]) + ', ' + \
                      format(percent, '.2f') + '% registered and ' +\
                      format(voted, '.2f') + '% voted.\n')
    
    return r_percent_list, r_voted_list

# Performs voter turnout calculations
def voter_turnout(voted_list_1, num_years_1):

    # loop determines calculates of years voter turnout < 60%
    less_voted_1 = 0
    for num in range(len(voted_list_1)):
        if voted_list_1[num] < 60:
            less_voted_1 += 1
    # loop calculates the % of years voter turnout > 80%
    year = 0
    for num in range(len(voted_list_1)):
        if voted_list_1[num] > 80:
            year += 1
    over_eighty_1 = (year/num_years_1)*100

    return less_voted_1, over_eighty_1


def main():
    nums = get_list() 
    year_list, eligible_voter_list, registered_voter_list, \
               num_ballots_cast = gen_lists(nums)
    percent_reg_list, voted_list = create_report(year_list, eligible_voter_list, registered_voter_list,\
                  num_ballots_cast)
    num_years = len(year_list)
    avg_percent_reg = (sum(percent_reg_list))/len(percent_reg_list)
    less_voted, over_eighty = voter_turnout(voted_list, num_years)
    
    print('\n\nThe total number of years listed:', str(num_years) + \
          '\n\nTotal ballots cast in all these years:', \
          format(sum(num_ballots_cast), ',.0f') + '\n\n' + \
          'Average percentage of eligible voters registered: ' + \
          format(avg_percent_reg, '.2f') + '%\n\nNumber of',\
          'years with less than 60% of registered voters casting ballots:',\
          format(less_voted, ',.0f'), '\n\n' +\
          'Percentage of years with more than 80% of registered voters',\
          'casting ballots:', format(over_eighty, '.1f') + '%',\
          '\n\nAn output file named REPORT-' + str(filename), \
          'has been successfully created.')
    print('\n\nThank you for using Voter View, goodbye.')


main()

# Close
data_file.close()
dataout.close()

##Testing -
##
##    file used: MidTermElections.txt
##    results: the user report file aggregates the data properly and shell
##    window outputs/displays data as expected.
##    Data output concurs with external calculations.
##
##    file used: PresidentialElections.txt
##    results: the user report file aggregates the data properly and shell
##    window outputs/displays data as expected.
##    Data output concurs with external calculations.
