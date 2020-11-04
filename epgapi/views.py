from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from epgapi.models import context_info
# Create your views here.
import json

def ctxinfo(request):
    if request.method == "GET":
        contexts={}
        query_ctx= context_info.objects.all()
        for ctx in query_ctx:
            contexts[ctx.ctxname]=ctx.vpnrd
        return JsonResponse({"status":"BS.200","all_contexts":contexts,"msg":"query contexts sucess."})
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        key_flag = req.get("name") and req.get("vpnrd") and len(req) == 2

        ctxname = req["name"]
        ctxvpnrd = req["vpnrd"]
        # title返回的是一个list
        ctx_exist = context_info.objects.filter(ctxname=ctxname)
        if len(ctx_exist) != 0:
            return JsonResponse({"status": "BS.400", "msg": "context aleady exist,fail to publish."})
        add_context = context_info(ctxname=ctxname, vpnrd=ctxvpnrd,ints=[1,2,3,4])
        add_context.save()
        return JsonResponse({"status": "BS.200", "msg": "publish article sucess."})
    else:
        return JsonResponse({"status": "BS.400", "message": "please check param."})