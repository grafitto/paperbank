var app = angular.module("App", []);

app.controller("PaperController", ["$scope", "$http", function ($scope, $http) {
    $scope.data = {}
    $scope.courses = {}
    $scope.units = {}
    $scope.years = []

    $scope.init = function () {
        for (let i = 0; i < 20; i++) {
            $scope.years[i] = 1997 + i;
        }
        console.log($scope.years);
    }
    
    $scope.departmentOnChange = function () {
        let departmentId = $scope.data.selectedDepartment;
        $http.get("/api/department/" + $scope.data.selectedDepartment + "/course").then(function (resp) {
            $scope.courses = resp.data.objects;
        }, function (err) {
            console.log(err);
        })
    }
    $scope.courseOnChange = function () {
        let course = $scope.data.selectedCourse;
        if (course != null) {
            if (course.unit != null) {
                console.log("Found units...");
                $scope.units = course.unit;
            } else {
                let courseId = course.id;
                console.log("Fetching units...");
                $http.get("/api/course/" + courseId + "/unit").then(function (resp) {
                    //$scope.units = resp.data.objects;
                    console.log(resp.data.objects);
                }, function (err) {
                    console.log(err);
                });
            }
        }
    }
}]);

app.controller("UnitController", ["$scope", "$http", function ($scope, $http) {
    $scope.data = {}
    $scope.courses = {}

    $scope.departmentOnChange = function () {
        let departmentId = $scope.data.selectedDepartment;
        $http.get("/api/department/" + departmentId + "/course").then(function (resp) {
            $scope.courses = resp.data.objects;
        }, function (err) {
            console.log(err);
        })
    }
    
}])