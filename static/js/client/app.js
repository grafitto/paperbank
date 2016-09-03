var app = angular.module("app", ['ngRoute']);

app.config(['$routeProvider',function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl: "partials/main.html",
        controller: "MainController"
    })
    .when("/course/:courseId/units", {
        templateUrl: "partials/units.html",
        controller: "UnitsController"
    });
}])
.run(["$rootScope", "Server", function ($rootScope, Server) {
    $rootScope.departments = {};

    $rootScope.$on("$routeChangeSuccess", function(data){
		
    });

    Server.departmentsPopulate()
       .then(function (resp) {
           $rootScope.departments = resp.objects;
       }, function (err) {
           console.log("Error");
           console.log(err);
       })
}])
.directive('a', function () {
    return {
        restrict: 'E',
        link: function (scope, elem, attrs) {
            if (attrs.ngClick) {
                elem.on('click', function (e) {
                    e.preventDefault();
                });
            }
        }
    };
});