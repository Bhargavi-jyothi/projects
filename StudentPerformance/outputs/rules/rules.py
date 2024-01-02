def findDecision(obj): #obj[0]: gender, obj[1]: StageID, obj[2]: GradeID, obj[3]: raisedhands, obj[4]: VisITedResources, obj[5]: AnnouncementsView, obj[6]: Discussion, obj[7]: ParentAnsweringSurvey, obj[8]: ParentschoolSatisfaction, obj[9]: StudentAbsenceDays
	# {"feature": "StudentAbsenceDays", "instances": 480, "metric_value": 1.5486, "depth": 1}
	if obj[9] == 'Under-7':
		# {"feature": "raisedhands", "instances": 289, "metric_value": 1.1952, "depth": 2}
		if obj[3]>0:
			# {"feature": "VisITedResources", "instances": 288, "metric_value": 1.1828, "depth": 3}
			if obj[4]>0:
				# {"feature": "Discussion", "instances": 287, "metric_value": 1.1698, "depth": 4}
				if obj[6]>2:
					# {"feature": "AnnouncementsView", "instances": 285, "metric_value": 1.1565, "depth": 5}
					if obj[5]<=96.79532905801415:
						# {"feature": "ParentschoolSatisfaction", "instances": 283, "metric_value": 1.1571, "depth": 6}
						if obj[8] == 'Good':
							# {"feature": "GradeID", "instances": 200, "metric_value": 1.0229, "depth": 7}
							if obj[2] == 'G-02':
								# {"feature": "ParentAnsweringSurvey", "instances": 57, "metric_value": 0.973, "depth": 8}
								if obj[7] == 'Yes':
									# {"feature": "gender", "instances": 40, "metric_value": 0.9097, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 22, "metric_value": 0.8454, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 18, "metric_value": 0.9641, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[7] == 'No':
									# {"feature": "gender", "instances": 17, "metric_value": 0.9774, "depth": 9}
									if obj[0] == 'F':
										# {"feature": "StageID", "instances": 15, "metric_value": 0.9968, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'M'
										else: return 'M'
									elif obj[0] == 'M':
										return 'M'
									else: return 'M'
								else: return 'M'
							elif obj[2] == 'G-08':
								# {"feature": "gender", "instances": 50, "metric_value": 1.1188, "depth": 8}
								if obj[0] == 'M':
									# {"feature": "ParentAnsweringSurvey", "instances": 33, "metric_value": 1.0648, "depth": 9}
									if obj[7] == 'Yes':
										# {"feature": "StageID", "instances": 32, "metric_value": 1.0794, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[7] == 'No':
										return 'M'
									else: return 'M'
								elif obj[0] == 'F':
									# {"feature": "StageID", "instances": 17, "metric_value": 0.7871, "depth": 9}
									if obj[1] == 'MiddleSchool':
										# {"feature": "ParentAnsweringSurvey", "instances": 17, "metric_value": 0.7871, "depth": 10}
										if obj[7] == 'Yes':
											return 'H'
										else: return 'H'
									else: return 'H'
								else: return 'H'
							elif obj[2] == 'G-07':
								# {"feature": "ParentAnsweringSurvey", "instances": 41, "metric_value": 0.9789, "depth": 8}
								if obj[7] == 'Yes':
									# {"feature": "gender", "instances": 35, "metric_value": 0.9852, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 22, "metric_value": 0.976, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[7] == 'No':
									# {"feature": "gender", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									else: return 'H'
								else: return 'H'
							elif obj[2] == 'G-04':
								# {"feature": "gender", "instances": 18, "metric_value": 0.7642, "depth": 8}
								if obj[0] == 'F':
									# {"feature": "ParentAnsweringSurvey", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[7] == 'Yes':
										# {"feature": "StageID", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									elif obj[7] == 'No':
										# {"feature": "StageID", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[0] == 'M':
									# {"feature": "StageID", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[1] == 'lowerlevel':
										# {"feature": "ParentAnsweringSurvey", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[7] == 'Yes':
											return 'H'
										else: return 'H'
									else: return 'H'
								else: return 'H'
							elif obj[2] == 'G-06':
								# {"feature": "gender", "instances": 18, "metric_value": 0.9183, "depth": 8}
								if obj[0] == 'F':
									# {"feature": "ParentAnsweringSurvey", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7] == 'Yes':
										# {"feature": "StageID", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									elif obj[7] == 'No':
										# {"feature": "StageID", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[0] == 'M':
									# {"feature": "StageID", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'MiddleSchool':
										# {"feature": "ParentAnsweringSurvey", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[7] == 'Yes':
											return 'H'
										elif obj[7] == 'No':
											return 'M'
										else: return 'M'
									else: return 'H'
								else: return 'H'
							elif obj[2] == 'G-11':
								# {"feature": "ParentAnsweringSurvey", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[7] == 'Yes':
									# {"feature": "gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0] == 'F':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'HighSchool':
											return 'H'
										else: return 'H'
									elif obj[0] == 'M':
										# {"feature": "StageID", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'HighSchool':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[7] == 'No':
									return 'M'
								else: return 'M'
							elif obj[2] == 'G-12':
								# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0] == 'F':
									# {"feature": "StageID", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1] == 'HighSchool':
										# {"feature": "ParentAnsweringSurvey", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[7] == 'Yes':
											return 'H'
										else: return 'H'
									else: return 'H'
								else: return 'H'
							elif obj[2] == 'G-09':
								return 'M'
							elif obj[2] == 'G-10':
								# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == 'M':
									# {"feature": "StageID", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'HighSchool':
										# {"feature": "ParentAnsweringSurvey", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == 'Yes':
											return 'M'
										else: return 'M'
									else: return 'M'
								else: return 'M'
							else: return 'M'
						elif obj[8] == 'Bad':
							# {"feature": "ParentAnsweringSurvey", "instances": 83, "metric_value": 1.1786, "depth": 7}
							if obj[7] == 'No':
								# {"feature": "GradeID", "instances": 58, "metric_value": 1.0351, "depth": 8}
								if obj[2] == 'G-08':
									# {"feature": "gender", "instances": 19, "metric_value": 1.087, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 14, "metric_value": 1.2871, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[0] == 'F':
										return 'M'
									else: return 'M'
								elif obj[2] == 'G-02':
									# {"feature": "gender", "instances": 18, "metric_value": 1.1221, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 13, "metric_value": 0.6194, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'M'
										else: return 'M'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[2] == 'G-07':
									# {"feature": "gender", "instances": 11, "metric_value": 0.8659, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									else: return 'M'
								elif obj[2] == 'G-06':
									# {"feature": "gender", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0] == 'F':
										# {"feature": "StageID", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[0] == 'M':
										# {"feature": "StageID", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									else: return 'M'
								elif obj[2] == 'G-04':
									return 'M'
								elif obj[2] == 'G-09':
									return 'M'
								elif obj[2] == 'G-12':
									return 'M'
								elif obj[2] == 'G-11':
									return 'M'
								else: return 'M'
							elif obj[7] == 'Yes':
								# {"feature": "GradeID", "instances": 25, "metric_value": 1.2023, "depth": 8}
								if obj[2] == 'G-07':
									# {"feature": "gender", "instances": 8, "metric_value": 1.4056, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 6, "metric_value": 1.2516, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[0] == 'F':
										return 'H'
									else: return 'H'
								elif obj[2] == 'G-02':
									# {"feature": "gender", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									elif obj[0] == 'F':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'H'
										else: return 'H'
									else: return 'H'
								elif obj[2] == 'G-08':
									# {"feature": "gender", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'H'
										else: return 'H'
									elif obj[0] == 'F':
										return 'M'
									else: return 'M'
								elif obj[2] == 'G-04':
									return 'M'
								elif obj[2] == 'G-10':
									return 'M'
								elif obj[2] == 'G-11':
									return 'H'
								elif obj[2] == 'G-06':
									return 'M'
								else: return 'M'
							else: return 'M'
						else: return 'M'
					elif obj[5]>96.79532905801415:
						return 'H'
					else: return 'H'
				elif obj[6]<=2:
					# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'M':
						return 'L'
					elif obj[0] == 'F':
						return 'H'
					else: return 'H'
				else: return 'L'
			elif obj[4]<=0:
				return 'L'
			else: return 'L'
		elif obj[3]<=0:
			return 'L'
		else: return 'L'
	elif obj[9] == 'Above-7':
		# {"feature": "VisITedResources", "instances": 191, "metric_value": 1.0845, "depth": 2}
		if obj[4]<=64.70251863116054:
			# {"feature": "AnnouncementsView", "instances": 146, "metric_value": 0.8276, "depth": 3}
			if obj[5]<=72.3492828478364:
				# {"feature": "raisedhands", "instances": 143, "metric_value": 0.7988, "depth": 4}
				if obj[3]<=56.12619626816205:
					# {"feature": "ParentAnsweringSurvey", "instances": 135, "metric_value": 0.7069, "depth": 5}
					if obj[7] == 'No':
						# {"feature": "Discussion", "instances": 100, "metric_value": 0.5574, "depth": 6}
						if obj[6]<=31.07:
							# {"feature": "GradeID", "instances": 59, "metric_value": 0.3576, "depth": 7}
							if obj[2] == 'G-02':
								# {"feature": "ParentschoolSatisfaction", "instances": 23, "metric_value": 0.258, "depth": 8}
								if obj[8] == 'Bad':
									# {"feature": "gender", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'L'
										else: return 'L'
									elif obj[0] == 'F':
										return 'L'
									else: return 'L'
								elif obj[8] == 'Good':
									return 'L'
								else: return 'L'
							elif obj[2] == 'G-07':
								return 'L'
							elif obj[2] == 'G-08':
								# {"feature": "gender", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[0] == 'M':
									# {"feature": "ParentschoolSatisfaction", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[8] == 'Bad':
										# {"feature": "StageID", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'L'
										else: return 'L'
									elif obj[8] == 'Good':
										return 'L'
									else: return 'L'
								elif obj[0] == 'F':
									return 'L'
								else: return 'L'
							elif obj[2] == 'G-04':
								# {"feature": "ParentschoolSatisfaction", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[8] == 'Bad':
									return 'L'
								elif obj[8] == 'Good':
									return 'M'
								else: return 'M'
							elif obj[2] == 'G-12':
								# {"feature": "gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0] == 'M':
									return 'L'
								elif obj[0] == 'F':
									return 'M'
								else: return 'M'
							elif obj[2] == 'G-05':
								return 'L'
							elif obj[2] == 'G-06':
								return 'L'
							elif obj[2] == 'G-10':
								return 'L'
							elif obj[2] == 'G-11':
								return 'L'
							else: return 'L'
						elif obj[6]>31.07:
							# {"feature": "gender", "instances": 41, "metric_value": 0.7593, "depth": 7}
							if obj[0] == 'M':
								# {"feature": "GradeID", "instances": 30, "metric_value": 0.8813, "depth": 8}
								if obj[2] == 'G-02':
									# {"feature": "ParentschoolSatisfaction", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[8] == 'Bad':
										return 'L'
									elif obj[8] == 'Good':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'L'
										else: return 'L'
									else: return 'L'
								elif obj[2] == 'G-04':
									# {"feature": "ParentschoolSatisfaction", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[8] == 'Bad':
										# {"feature": "StageID", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'L'
										else: return 'L'
									elif obj[8] == 'Good':
										return 'M'
									else: return 'M'
								elif obj[2] == 'G-07':
									# {"feature": "ParentschoolSatisfaction", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[8] == 'Bad':
										# {"feature": "StageID", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'M'
										else: return 'M'
									elif obj[8] == 'Good':
										return 'L'
									else: return 'L'
								elif obj[2] == 'G-08':
									return 'L'
								elif obj[2] == 'G-05':
									return 'L'
								elif obj[2] == 'G-12':
									return 'L'
								elif obj[2] == 'G-11':
									return 'L'
								elif obj[2] == 'G-06':
									return 'M'
								else: return 'M'
							elif obj[0] == 'F':
								return 'L'
							else: return 'L'
						else: return 'L'
					elif obj[7] == 'Yes':
						# {"feature": "ParentschoolSatisfaction", "instances": 35, "metric_value": 0.9518, "depth": 6}
						if obj[8] == 'Good':
							# {"feature": "Discussion", "instances": 25, "metric_value": 0.795, "depth": 7}
							if obj[6]<=66:
								# {"feature": "GradeID", "instances": 20, "metric_value": 0.8813, "depth": 8}
								if obj[2] == 'G-07':
									# {"feature": "gender", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[1] == 'MiddleSchool':
											return 'L'
										else: return 'L'
									elif obj[0] == 'F':
										return 'L'
									else: return 'L'
								elif obj[2] == 'G-02':
									# {"feature": "gender", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[0] == 'M':
										# {"feature": "StageID", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[1] == 'lowerlevel':
											return 'L'
										else: return 'L'
									elif obj[0] == 'F':
										return 'M'
									else: return 'M'
								elif obj[2] == 'G-08':
									return 'L'
								elif obj[2] == 'G-09':
									return 'L'
								elif obj[2] == 'G-04':
									return 'M'
								else: return 'M'
							elif obj[6]>66:
								return 'L'
							else: return 'L'
						elif obj[8] == 'Bad':
							# {"feature": "Discussion", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[6]<=70:
								# {"feature": "GradeID", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[2] == 'G-06':
									return 'M'
								elif obj[2] == 'G-07':
									# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == 'F':
										return 'M'
									elif obj[0] == 'M':
										return 'L'
									else: return 'L'
								elif obj[2] == 'G-04':
									return 'M'
								elif obj[2] == 'G-02':
									return 'M'
								elif obj[2] == 'G-08':
									return 'M'
								else: return 'M'
							elif obj[6]>70:
								return 'L'
							else: return 'L'
						else: return 'M'
					else: return 'L'
				elif obj[3]>56.12619626816205:
					# {"feature": "Discussion", "instances": 8, "metric_value": 1.4056, "depth": 5}
					if obj[6]>17:
						# {"feature": "gender", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0] == 'F':
							# {"feature": "GradeID", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2] == 'G-08':
								# {"feature": "ParentschoolSatisfaction", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8] == 'Bad':
									return 'H'
								elif obj[8] == 'Good':
									return 'M'
								else: return 'M'
							elif obj[2] == 'G-07':
								return 'M'
							else: return 'M'
						elif obj[0] == 'M':
							return 'M'
						else: return 'M'
					elif obj[6]<=17:
						return 'L'
					else: return 'L'
				else: return 'M'
			elif obj[5]>72.3492828478364:
				return 'M'
			else: return 'M'
		elif obj[4]>64.70251863116054:
			# {"feature": "StageID", "instances": 45, "metric_value": 0.7768, "depth": 3}
			if obj[1] == 'MiddleSchool':
				# {"feature": "ParentschoolSatisfaction", "instances": 27, "metric_value": 0.7254, "depth": 4}
				if obj[8] == 'Good':
					# {"feature": "AnnouncementsView", "instances": 25, "metric_value": 0.4022, "depth": 5}
					if obj[5]<=62:
						return 'M'
					elif obj[5]>62:
						# {"feature": "Discussion", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[6]>40:
							return 'M'
						elif obj[6]<=40:
							# {"feature": "raisedhands", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]>75:
								return 'M'
							elif obj[3]<=75:
								return 'L'
							else: return 'L'
						else: return 'M'
					else: return 'M'
				elif obj[8] == 'Bad':
					# {"feature": "gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'F':
						return 'H'
					elif obj[0] == 'M':
						return 'L'
					else: return 'L'
				else: return 'H'
			elif obj[1] == 'lowerlevel':
				# {"feature": "raisedhands", "instances": 17, "metric_value": 0.6402, "depth": 4}
				if obj[3]>19:
					# {"feature": "Discussion", "instances": 15, "metric_value": 0.3534, "depth": 5}
					if obj[6]>10:
						return 'M'
					elif obj[6]<=10:
						# {"feature": "GradeID", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2] == 'G-02':
							return 'H'
						elif obj[2] == 'G-04':
							return 'M'
						else: return 'M'
					else: return 'H'
				elif obj[3]<=19:
					# {"feature": "GradeID", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'G-04':
						return 'L'
					elif obj[2] == 'G-02':
						return 'M'
					else: return 'M'
				else: return 'L'
			elif obj[1] == 'HighSchool':
				return 'H'
			else: return 'H'
		else: return 'M'
	else: return 'L'
