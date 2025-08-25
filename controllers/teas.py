from fastapi import APIRouter, HTTPException
from models.tea_data import teas_db

router=APIRouter()

@router.get('/teas')
def get_teas():
    return teas_db

@router.get('/teas/{tea_id}')
def get_single_tea(tea_id:int):
    for tea in teas_db['teas']:
        if tea['id']==tea_id:
            return tea
    raise HTTPException(status_code=404,detail='Tea not found')


@router.post('/teas')
def create_tea(tea: dict):
    teas_db['teas'].append(tea)
    return tea

@router.put('/teas/{tea_id}')
def update_tea(tea_id:int,tea:dict):
    
    for excisting_tea in teas_db['teas']:
        if excisting_tea['id']==tea_id:
            excisting_tea.update(tea)
            return excisting_tea
        
    raise HTTPException(status_code=404, detail="Tea not found")

@router.delete('/teas/{tea_id}')
def delete_tea(tea_id:int):
    for tea in teas_db['teas']:
        if tea['id']==tea_id:
            teas_db['teas'].remove(tea)
            return {"message":f" Tea with id {tea_id} is deleted"}
        
    raise HTTPException(status_code=404, detail="Tea not found")
    