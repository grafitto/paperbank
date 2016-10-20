var app = angular.module("app");

app.factory("Server", ["$http", "$q", function ($http, $q) {
    let server = {};
    let baseUrl = "/api";
    
    server.departments = function () {
        let deferred = $q.defer();
        $http.get(baseUrl + "/department")
            .success(function(resp) {
                deferred.resolve(resp);
            })
            .error(function(err) {
                deferred.reject(err);
            })
        return deferred.promise;
    }
    server.department = function (id) {
        let deferred = $q.defer();
        $http.get(baseUrl + "/department/" + id)
            .success(function (resp) {
                deferred.resolve(resp);
            })
            .error(function (err) {
                deferred.reject(err);
            });
        return deferred.promise;
    }
    server.course = function (courseId) {
        let deferred = $q.defer();
        $http.get(baseUrl + "/course/" + courseId)
            .success(function (resp) {
                resp.unit.forEach( function(unit, index) {
                    $http.get(baseUrl + "/unit/" + unit.id)
                        .success(function(resp){
                            unit["paper"] = resp.paper;
                        })
                });
                console.log(resp);
                deferred.resolve(resp);
            })
            .error(function (err) {
                deferred.reject(err);
            });
        return deferred.promise;
    }
    server.departmentsPopulate = function(){
        let deferred = $q.defer();
        $http.get(baseUrl + "/department")
            .success(function(resp){
                deferred.resolve(resp);
            })
            .error(function(err){
                deferred.reject(err);
            })

        return deferred.promise;
    }
    server.searchPaper = function(query){
        let deferred = $q.defer();
        $http.get(baseUrl + "/paper?q=" + JSON.stringify(query))
            .success(function(resp){
                deferred.resolve(resp);
            })
            .error(function(err){
                deferred.reject(err);
            })
        return deferred.promise;
    }
    server.paper = function (id) {
        let deferred = $q.defer();
        $http.get(baseUrl + "/paper/" + id)
            .success(function (resp) {
                deferred.resolve(resp);
            })
            .error(function (err) {
                deferred.reject(err);
            })
        return deferred.promise;
    }
    return server;
}]);