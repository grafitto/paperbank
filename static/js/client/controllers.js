var app = angular.module("app");

app.controller("MainController", ["$scope", "$rootScope", "Server", function ($scope, $rootScope, Server) {
    $scope.departments = $rootScope.departments;
    $scope.course = {};
    $scope.unitsEmpty = false;
    let cache = {};

    $scope.getUnits = function (courseId) {
        if (cache[courseId] != undefined) {
            $scope.course = cache[courseId];
            $scope.unitsEmpty = $scope.course.unit.length == 0;
            console.log("Got from cache...");
        } else {
            Server.course(courseId)
            .then(function (resp) {
                $scope.course = resp;
                cache[courseId] = resp;
                $scope.unitsEmpty = $scope.course.unit.length == 0;
                console.log("Fetched then cached...");
            }, function (err) {
                console.log(err);
            })
        }
        //
    }
}]);
