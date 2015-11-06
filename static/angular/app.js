window.addEventListener("hashchange", function(){
   console.log("Hash changed") ;
   console.log(window.location.hash);
});

 var app = angular.module("myApp",['ngRoute']);

app.config(['$httpProvider','$routeProvider', function($httpProvider, $routeProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    
    $routeProvider
        .when('/', {
            templateUrl : "/static/angular/partials/first.html",
            controller : "firstController"
        })
        .when('/second/:num',{
            templateUrl: "/static/angular/partials/second.html",
            controller: "secondController"
        })
   
}]);

app.controller('mainController', ['$scope','$http','$location', function($scope, $http, $location){
       
    
        console.log($location.path());
        $scope.posts =[];
        $http.get("/api/api_demo/")
            .success(function(data){
              angular.forEach(data, function(value, key){
                 console.log(value);
                 $scope.posts.push(value);
                });
            })
            .error(function(error){
                console.log(error);
            });
            
       
       $scope.newPost = '';
       $scope.addMe = function(){
            
            $http({
            url: "/api/api_demo/", 
            data: { post: $scope.newPost }, 
            method: "POST",
            //headers: {'X-CSRFToken': $cookies['csrftoken']}
            
        })
        .success(function(data){
            console.log(data);
     
            $scope.posts.push(data);
            
            $scope.newPost = '';
            
        })
        .error(function(data){
            console.log(data);
        });

       };
       
        
    
}]);



app.controller('firstController', ['$scope', function($scope){
    $scope.name = "Anish";
        
}]); 

app.controller('secondController', ['$scope', '$routeParams', function($scope, $routeParams){
    $scope.num = $routeParams.num;
    
}]); 


app.directive('demoDirective', function(){
    return {
        restrict: 'AE',
        templateUrl: '/static/angular/directives/showPost.html',
        replace: true
    }
})