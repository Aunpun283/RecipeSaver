import pymongo
from bson import ObjectId, json_util
from django.http import JsonResponse
db_client = pymongo.MongoClient("mongodb+srv://aunpun:goodpassword@cluster0.a8gk28i.mongodb.net/?retryWrites=true&w=majority")
database = db_client["recipesaver"]
    

recipes_coll = database["recipes"]

def add_recipe(request,): 
    name = request.GET.get("name")
    ownerid = request.GET.get("ownerid")
    data_to_add = {"name":str(name),"ingredients":[],"instructions":[],"ownerid":ownerid}
    try:
        inserted_data = recipes_coll.insert_one(data_to_add)

     
    except Exception as e: return JsonResponse({"status":"failed", "error": str(e)})
    return JsonResponse({"status":"success", })
from django.http import JsonResponse

def fetch_recipe_list_with_ownerid(request):
    ownerid = request.GET.get("ownerid")
    query = {"ownerid": ownerid}
    try:
        fetched_data_cursor = recipes_coll.find(query)

    except Exception as e:
        return JsonResponse({"status": "failed", "error": str(e)})

    return JsonResponse({"status": "success", "data": json_util.dumps(fetched_data_cursor)})
def fetch_recipe(request):
    id = request.GET.get("id")
    query = {"_id":ObjectId(id)}
    try:
        fetched_data_cursor = recipes_coll.find_one(query)
    except Exception as e: return JsonResponse({"status": "failed", "error": str(e)})
    return JsonResponse({"status": "success", "data": json_util.dumps(fetched_data_cursor)})
def add_ingredient(request):
    id = request.GET.get("id")
    ingred = request.GET.get("ingred")
    amount  = request.GET.get("amou")
    unit = request.GET.get("unit")
    query = {"_id":ObjectId(id)}
    data2add = {"ingred":ingred,"amount":amount,"unit":unit}
    try:
        old_Data = recipes_coll.find_one(query)
        ingred_list = list(old_Data["ingredients"])
        ingred_list.append(data2add)
        recipes_coll.update_one(query,{"$set":{"ingredients":ingred_list}})
    except Exception as e: return JsonResponse({"status": "failed", "error": str(e)})
    return JsonResponse({"status": "success",})
def add_instruction(request):
    id = request.GET.get("id")
    instruc = request.GET.get("instruc")
    query = {"_id":ObjectId(id)}
    data2add = {"instruc":instruc}
    try:
        old_Data = recipes_coll.find_one(query)
        ingred_list = list(old_Data["instructions"])
        ingred_list.append(data2add)
        recipes_coll.update_one(query,{"$set":{"instructions":ingred_list}})
    except Exception as e: return JsonResponse({"status": "failed", "error": str(e)})
    return JsonResponse({"status": "success",})
def del_recipe(request):
   id = request.GET.get("id")
   query = {"_id":ObjectId(id)}
   try:
       recipes_coll.delete_one(query)
   except Exception as e: return JsonResponse({"status": "failed", "error": str(e)})
   return JsonResponse({"status":"success"})