from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):

    
    def get(self, name):
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.findByName(name):
            return {'message': "An store called '{}' already exists".format(name)}, 400
        store = StoreModel(name)
        try:
            store.saveToDb()
        except:
            return {"message": "An error occurred adding the store"}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.deleteFromDb()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
