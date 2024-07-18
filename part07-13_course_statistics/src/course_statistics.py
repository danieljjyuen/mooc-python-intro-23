# Write your solution here
import urllib.request
import json


def retrieve_all():
    link ="https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(link)
    content = request.read()
    parsed = json.loads(content)
    result = []

    for obj in parsed:
        if obj["enabled"] == True:
            result.append((obj["fullName"], obj["name"], obj["year"], sum(obj["exercises"])))
    
    return result

def retrieve_course(course_name:str):
    link = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    link = link.replace("****", course_name)
    request = urllib.request.urlopen(link)
    content = request.read()
    parsed = json.loads(content)
    #print(parsed["0"])

    students = 0
    hours =0
    hours_average = 0
    exercises = 0
    exercises_average =0

    for index in parsed:
        if parsed[index]["students"] > students:
            students = parsed[index]["students"]
        hours+= parsed[index]["hour_total"]
        exercises+= parsed[index]["exercise_total"]
    
    hours_average = hours//students
    exercises_average = exercises//students

    result = {}
    result["weeks"] = len(parsed)
    result["students"] = students
    result["hours"] = hours
    result["hours_average"] = hours_average
    result["exercises"] = exercises
    result["exercises_average"] = exercises_average

    return result

#print(retrieve_course("docker2019"))


#{'0': {'students': 220, 'hour_total': 286, 
# 'exercise_total': 218, 
# 'hours': [None, 176, 11, 3, 1, 1, None, None, 6]}, 
# '1':
#  {'students': 176, 'hour_total': 2421, 'exercise_total': 2748, 
# 'hours': [None, 6, 3, 3, 4, 9, 5, 8, 13, 4, 28, 1, 14, 2, 3, 20, 2, 4, 3, None, 15, 1, 1, None, 6, 5, None, 1, 2, None, 8, None, None, None, None, 1, None, None, None, None, 2, 2]},
#  '2': {'students': 143, 'hour_total': 1862, 'exercise_total': 1343, 
# 'hours': [None, 1, 1, 5, 5, 8, 8, 3, 10, 7, 21, 1, 11, 6, 1, 11, 7, 2, 4, None, 10, None, None, None, 4, 3, 1, None, None, None, 3, 2, None, None, None, 5]}, 
# '3': {'students': 99, 'hour_total': 1397, 'exercise_total': 679, 'hours': [None, 1, 2, 1, 2, 4, 7, 5, 10, 1, 17, 1, 3, 3, 5, 7, 2, 1, 1, None, 8, None, 1, None, 3, 3, 1, None, None, None, 1, None, 1, None, None, 8]}}





#[{"week":7,
# "exercises":[17,13,13,8,6,5,11],
# "enabled":false,
# "miniproject":false,
# "peerReviewOpen":false,
# "extension":false,
# "_id":"59f883227655fe0034b4dfe5","year":2017,
# "term":"syksy","fullName":"Ohjelmistotuotanto",
# "name":"ohtus17",
# "url":"https://github.com/mluukkai/ohjelmistotuotanto2017/wiki/Ohjelmistotuotanto-syksy-2017","__v":
# 7},{"week":8,"exercises":[6,14,19,22,21,21,23,23],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5a576ac24d91600059c09180","year":1970,"term":"Unknown term","fullName":"Full stack -websovelluskehitys","name":"fs","url":"https://fullstack-hy.github.io","__v":9},{"week":8,"exercises":[6,14,19,22,21,21,23,23],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5a7f50aa9b73740051c69898","year":2018,"term":"Unknown term","fullName":"Open Full Stack 2018","name":"ofs","url":"http://fullstackopen.github.io","__v":8},{"week":7,"exercises":[0,17,13,13,8,6,6,11],"enabled":false,"miniproject":true,"peerReviewOpen":false,"extension":false,"_id":"5bb48ca56ec4c800e33cb76f","year":2018,"term":"syksy","fullName":"Ohjelmistotuotanto","name":"ohtu2018","url":"https://github.com/mluukkai/ohjelmistotuotanto2018/wiki/Ohjelmistotuotanto-syksy-2018","__v":7},{"week":4,"exercises":[0,8,6,7,0,0,0,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5be43839e90ef000b62e8ca4","year":2018,"term":"fall","fullName":"Beta DevOps with Docker","name":"docker-beta","url":"https://docker-hy.github.io","__v":3},{"week":7,"exercises":[0,11,16,16,15,15,15,15],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5be5dfaeca8b21009ac43d35","year":2018,"term":"syksy","fullName":"Web-palvelinohjelmointi Ruby on Rails","name":"rails2018","url":"https://github.com/mluukkai/WebPalvelinohjelmointi2018","__v":7},{"week":1,"exercises":[0,9,6,7,0,0,0,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5c17f2fdcccfd100f9c6a260","year":2018,"term":"christmas","fullName":"DevOps with Docker","name":"docker18","url":"https://docker-hy.github.io/","__v":3},{"week":8,"exercises":[6,14,20,22,21,21,21,20,0],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":true,"_id":"5c39d27776e25b01007e7a12","year":2019,"term":"kev\xc3\xa4t","fullName":"Full stack websovelluskehitys","name":"fullstack2019","url":"https://fullstack-hy2019.github.io/","__v":11},{"week":8,"exercises":[0,4,4,4,5,3,3,4],"enabled":false,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5c3dd379e2ecb8022bb75407","year":2019,"term":"Fall","fullName":"Cloud Computing Fundamentals","name":"CCFUN","url":"https://ccfun.fi/home","__v":8},{"week":0,"exercises":[6,14,20,22,22,22,21,21,26,27],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":true,"_id":"5c7f97d3b7e42b00495261de","year":2020,"term":"Year","fullName":"Full Stack Open 2020","name":"ofs2019","url":"https://fullstackopen.com/","__v":16},{"week":4,"exercises":[1,17,10,8,0,0,0,0],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5cb5bcd65e4c2f005281f7e7","year":2019,"term":"Year","fullName":"DevOps with Docker 2019","name":"docker2019","url":"https://docker-hy.github.io/","__v":4},{"week":1,"exercises":[1,17,10,8],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5e8ae0d2d9979700193caed4","name":"docker2020","url":"https://devopswithdocker.com/","term":"Year","year":2020,"fullName":"DevOps with Docker 2020","__v":0},{"week":1,"exercises":[0,13,8,7],"enabled":true,"miniproject":false,"peerReviewOpen":false,"extension":false,"_id":"5ebe6a8f54e7f10019becc15","name":"beta-dwk-20","url":"https://devopswithkubernetes.com","term":"Summer","year":2020,"fullName":"Beta DevOps with Kubernetes","__v":1}]'