/**
 * Created by yeti on 20.11.2014.
 */

badges = angular.module("badges", ["ngResource", "wu.masonry", "angularMoment"]);

angular.module("badges").config(['$interpolateProvider', '$resourceProvider', '$httpProvider' , function ($interpolateProvider, $resourceProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;

}]);

angular.module('badges').constant('angularMomentConfig', {
    preprocess: 'unix', // optional
    timezone: 'Europe/Bucharest' // optional
});

angular.module('badges').factory('_', ['$window',
      function($window) {
        return $window._;
      }
]);

angular.module('badges').factory('BadgeService', ['$resource', function BadgeService($resource) {
        return $resource('/api/1/badges/:id/', {
            id: '@id'
        });
    }
]);

angular.module("badges").controller("BadgesController", ["$scope", "BadgeService", "_", function BadgesController($scope, BadgeService, _) {

    BadgeService.query(function (data) {
        $scope.badges = data;
    });

}]);

angular.module("badges").controller("BadgeController", ["$scope", "BadgeService", "_", function BadgeController($scope, BadgeService, _) {

}])