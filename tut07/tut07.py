import os
import pandas as pd


def non_zero_bits(s): 
		count=0
		zeroes=0
		
		for k in range(len(s)):
			if((s[k])=='0'):
				zeroes+=1
			
		count=3-zeroes
		return count

bits_dict={}
ouyput_dictionary={}

def mini(contemp,dictionary_sub,f,rollno):
			for a in contemp:
				x=bits_dict[a]
				
	
				if x[0][1]!=0:
					if dictionary_sub.count(a)!=x[0][1]:
						if contemp.count(a)!=x[0][1]:
							diff=x[0][1]-contemp.count(a)
							while diff>0:
								f.append(a)
								diff-=1
					f.append(a)
				else:
					continue
			
			for z in dictionary_sub:
				x=bits_dict[z]
				
				if z in f:
					f.remove(z)
			if len(f)!=0:		
				if rollno in ouyput_dictionary:
					ouyput_dictionary[rollno].append(f)
				else:
					ouyput_dictionary[rollno]=[]
					ouyput_dictionary[rollno].append(f)
				return rollno

def non_zero_bits(s): 
		count=0
		zeroes=0
		
		for k in range(len(s)):
			if((s[k])=='0'):
				zeroes+=1
			
		count=3-zeroes
		return count

def check(submitted_dict,registered_dict,roll): 
	if roll in registered_dict:
		temp=registered_dict[roll].copy()
		n=len(temp)
		s=[]
		m=len(submitted_dict)
		if(n!=m):
			
			return mini(temp,submitted_dict,s,roll)
	

			
def feedback_not_submitted(): 

	
	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 
	path=os.getcwd()
	registered_file=pd.read_csv('course_registered_by_all_students.csv')
	registered_roll=registered_file['rollno'].values.tolist()
	registered_data=registered_file[['register_sem','schedule_sem','subno']].values.tolist()
	registered_sub=registered_file['subno'].values.tolist()

	
	unique_registered_roll=set(registered_roll)
	registered_dict={}
	
	i=0
	for a in registered_roll:
		if a in registered_dict:
			registered_dict[a].append(registered_sub[i])
		else:
			registered_dict[a]=[]
			registered_dict[a].append(registered_sub[i])
		
		i+=1
	
	i=0
	registered_data_dict={}
	for a in registered_sub:
		
		registered_data_dict[a]=[]
		registered_data_dict[a]=registered_data[i]
		i+=1

	
	
	submitted_file=pd.read_csv("course_feedback_submitted_by_students.csv")
	submitted_sub=submitted_file['course_code'].values.tolist()
	roll_sub=submitted_file['stud_roll'].values.tolist()
	dict_sub={}

	c=0
	for a in roll_sub:
		if a in dict_sub:
			dict_sub[a].append(submitted_sub[c])
		else:
			dict_sub[a]=[]
			dict_sub[a].append(submitted_sub[c])
		c+=1

	
	info_file=pd.read_csv('studentinfo.csv')
	ltp_file=pd.read_csv('course_master_dont_open_in_excel.csv')
	
	list_ltp=ltp_file['ltp'].values.tolist()
	sub_ltp=ltp_file['subno'].values.tolist()
	
	list_info=info_file[['Name','email','aemail','contact']].values.tolist()
	info_cont=info_file['contact'].values.tolist()
	
	
	info_roll=info_file['Roll No'].values.tolist()
	
	dict_info={}

	c=0
	for a in info_roll:
		if a in dict_info:
		
				dict_info[a].append(list_info[c])
		
		else:
			dict_info[a]=[]
		
			dict_info[a].append(list_info[c])
		
		c+=1
	

	c=0
	for a in sub_ltp:
		bits=non_zero_bits(list_ltp[c])
		if a in bits_dict:
			
			bits_dict[a].append([list_ltp[c],bits])
		else:
			bits_dict[a]=[]
			bits_dict[a].append([list_ltp[c],bits])
		
		c+=1
	
	s=[]
	for i in unique_registered_roll:
		if i in dict_sub:
			temp=check(dict_sub[i],registered_dict,i)
			s.append(temp)
		else:
			s.append(i)

	
	output_list=[]
	for i in ouyput_dictionary:
		for j in ouyput_dictionary[i]:
			for k in j:
				x=[]
				x.append(i)
				
			
			
				x.extend(registered_data_dict[k])
				p=dict_info[i]
				
				x.append(p[0][0])
				x.append(p[0][1])
				x.append(p[0][2])
				x.append(str(p[0][3]))
				
				
				output_list.append(x)
	
	output_data=pd.DataFrame(output_list,columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact'])
	
	output_data.to_excel(output_file_name)
	
	print(output_data.head())
