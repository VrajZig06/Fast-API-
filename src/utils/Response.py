def Response(msg:str,status:str,data : any) -> dict:
    return {
        "Status" : status,
        "Msg" : msg,
        "Data" : data
    }