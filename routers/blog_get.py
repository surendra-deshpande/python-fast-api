from fastapi import APIRouter, status, Response, APIRouter
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

#Order of API paths are important and are evaluated as they are mentioned. 
#if /all is defined after /id then /all will fail as id is expected to be an integer but all is interpreted and is a string
# hence the order is important. Matched one by one sequentially.
# @app.get('/all')
# def getAll():
#     return { 'index': 'all'}
@router.get('/all')
def getAll(page = 1, pageSize = 10):
    return {'message': f'Page : {page}, Page Size: {pageSize}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def getType(type: BlogType):
    return {'message': f'Type {type}'}

# @app.get('/{id}')
# def getIndex(id: int):
#     return { 'index': f'{id}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def getIndex(id: int, response: Response, page = 1, pageSize = 10):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message' : f'{id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return { 'index': f'Id : {id}, Page : {page}, Page Size : {pageSize} '}