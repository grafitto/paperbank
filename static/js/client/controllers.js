var app = angular.module("app");

app.controller("MainController", ["$scope", "$rootScope", "Server", function ($scope, $rootScope, Server) {
    $scope.departments = $rootScope.departments;
    $scope.course = {};
    $scope.unitsEmpty = false;
    $scope.breadCrumb = [];
    $scope.loading = false;
    $scope.isSearch = false;
    $scope.papers = [];

    $scope.$on('$viewContentLoaded', function(){
        Server.departmentsPopulate()
            .then(function (resp) {
                $scope.departments = resp.objects;
                console.log("Fetching departments...");
            }, function (err) {
                console.log("Error");
                console.log(err);
            })
    });
    $scope.search = function(){
        let q = $("#q").val();
        q = "%" + q + "%";
        //let query = {"filters":[{"or":[{"name":"title","op":"like","val": q},{"name":"lecturer","op":"like","val":q}]}]}
        let query = {filters:[{name:"title",op:"like",val:q}]};
        if(q == "%%"){
            $scope.isSearch = false;
        }else{
            $scope.isSearch = true;
        }
        $scope.loading = true;
        Server.searchPaper(query)
            .then(function(resp){
                $scope.loading = false;
                $scope.papers = resp.objects;
            },
            function(err){
                console.log(err);
            })
    }
    $scope.getUnits = function (courseId) {
            $scope.loading = true;
            Server.course(courseId)
                .then(function (resp) {
                    $scope.course = resp;
                    resp.objects.forEach(function(item){
                        console.log("item", item);
                        Server.paper(item.id)
                            .then(function(resp){
                                console.log(paper resp", resp);
                                item.paper = resp.object;
                            })
                    })
                    //Populate preadcrump
                    if($scope.breadCrumb.length > 1){
                        let first = $scope.breadCrumb.shift();
                        while($scope.breadCrumb.length){ $scope.breadCrumb.pop()}
                        $scope.breadCrumb.push(first);
                    }
                    $scope.breadCrumb.push(resp.title);
                    $scope.loading = false;
                }, function (err) {
                    console.log(err);
                })
        }

    $scope.populateBreadCrumb = function(text){
        while($scope.breadCrumb.length){ $scope.breadCrumb.pop()}
        $scope.breadCrumb.push(text);
    }

    $scope.preventDefaultA = function(){ return true;}
}]);


