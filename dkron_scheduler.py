from pydkron.client import DkronClient

dc=DkronClient(hosts=["192.168.0.159:8080","192.168.0.126:8080"])

jd={
"name":"job1",
"schedule":"@at 2021-03-10T15:11:00Z",
"tags":{
"role":"dkron:1"
},
"executor":"shell",
"executor_config":{
"command":"touch hellothere.txt"
}
}

job=dc.create_job(jd)
job.save()
job.run()
