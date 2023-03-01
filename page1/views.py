from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from firebase_admin import credentials, initialize_app, firestore

json = {
    "type": "service_account",
    "project_id": "society-management-syste-b0697",
    "private_key_id": "2801f045d917c9b4d126afc51c20eac7564b73c0",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCnkGni1PiyS+b3\nQD4EcqTjRxi8RAbUDcp3dFiIQYHp3pKz57TcDKX+SViirzUUxInApw1gXxb1vMKv\nuKmcD2Lc7dJNDqP8pVznoXTGAtTPT7YY3YTOB2fOiojh6r/vhjbhFI6Wqtt/Zr44\nnop//+CHWNxhH6lBSigBe6a6lj8YFSMFs5sQlKOnaUBs9VFkMzfKRQ3i0mxNHfva\nVEnRyahPOrkZPSkcUX1HDlvKYiGtsYUc5SXUY5NNGwVNAMqe7o0oZ7615BG01rjw\nd5k3b1aZQG0wrKpYvOTj97O1NP9QE9uhivHlZOsm8T1awSliBWnfXrTylwCNONsc\nkDCZQkHJAgMBAAECggEAL6G0D8hVd61u1sr6th32tCqiI+Y8gKv46VL31ae1a8sa\nraxIc6LezrV/ziL69k/WDp8OBN6S8sC5IOVfxV50TnQGK2Rlhixlh+yT+rOUVegF\nTfUuSri9L++ecIXgEJD46auDyt1/rqwAl6ytlywf4amHX851uPsA+0bwgqqx/cCR\n/lXqi2s10ydYNAjcCHwhZ/ohvrZWFvsLLpVv+OtNSl2CybtK+8aFFL2bZ37cWl5R\nO6HiPSDgkZsEH0egBKLl8k7QvU1+6fVlzGcU7eJmIWUKFI46YQspvjIIpneTYGw0\no5/n16dHu+nSZSFT468WR53UZP2/QU1zHeSKu+7ptwKBgQDmP9CNF6mo7yTyALO/\n0jugFZgsTNnQJ31X0PyO1xHz2WbNYN6Po00TQ8iG+Af7K8wvcGCzoHhSyeWnS4+y\nBx709Ib6EX5relPw72aq7w+oiS+bo5f+HOXOAFhcwZ6EJkaTu+apMCJUMgR0DPrf\nd+vI0DfonSWXRaeQOdMvpHhYuwKBgQC6TeHjYCC9funqbvZd1cQlNzvzBO1L4nFY\nvogSnmI6n+FGitJc8JjVLihqVFLpII+5ClnAqRsqmgn+1XONPgRsVGFZGvTuNTrT\nk87V9eDNmIZYJjMeSSJ43njtUAZXGvBsnDSswNe3L2NUz0XU4G7lhGvXyjXw3iHH\nuU4X2aIZSwKBgDl812pS7SZjxzqxGDAdoot+uMbezUdehLonUNetNStILZW7yPXe\nFQFpXCjuxrdcoRd7HHnc6A3roO5bPF57zqvkXcsUERdurISskVq+Y4916TAX8Xwd\n5PbBOU63fQeLsvVx5c56WSficSA0mXKwM2upKTxn+BnD52loNqVfkDi/AoGAfTvZ\nOlTl7Tug1fvdFFqbzUCBxexr7vS6qKL7KTjaYvoSHq82lU8ODU9Hz6H7UcaXlhVF\nG+MQ5eRCD9FAKZOkuYVHIvSh7HZPouXaxazQfqOmux6Cgjs7NvClbTC78lWjg/7E\n0dOXrgXmyZ3DHUP4h8QqEhZViCJppq4DtriO5F0CgYB+dDWAJS648ZjVTWb7Ozsx\nArEv+5hETt6kTOzosinsMYgkP21KsG9IvLXeB0Qu9FRZuRUOYzuXTe4BEDY7fSQc\ngNo7T3JXN65DQ0BqQf1N/ToSx3EZyiHhfkwP3JrCap6EgIpLTPToEMXqT32Pi5G6\nQiD0bq1ep3006UOD5EmHSg==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-hpz61@society-management-syste-b0697.iam.gserviceaccount.com",
    "client_id": "112130023676574660877",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hpz61%40society-management-syste-b0697.iam.gserviceaccount.com"
}

cred = credentials.Certificate(json)
firebase = initialize_app(cred)
db = firestore.client()


# Create your views here.
def home(request):
    comments = db.collection('comments').get()
    comments_list = [comments[i].to_dict()['comments'] for i in range(len(comments))]
    return render(request, 'home.html', {'comments': comments_list})


def submit_comment(request):
    ref = db.collection('comments')
    ref.document().set({'comments': request.GET['comment']})

    comments = db.collection('comments').get()
    comments_list = [comments[i].to_dict()['comments'] for i in range(len(comments))]
    return render(request, 'home.html', {'comments': comments_list})
