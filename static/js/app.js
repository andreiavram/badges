/**
 * Created by yeti on 20.11.2014.
 */

badges = angular.module("badges", ["ngResource", "wu.masonry", "angularMoment", "infinite-scroll"]);

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
    base_url = "/api/1/badges/:id/";
        return $resource('/api/1/badges/:id/', {
            id: '@id'
        }, {
            update_status: { method: "patch", isArray: false, url: base_url + "update/"}
        });
    }
]);

angular.module('badges').factory('EvenimentService', ['$resource', function EvenimentService($resource) {
        return $resource('/api/1/evenimente/:id/', {
            id: '@id'
        }, {
            "query": { method: "get", isArray: false }
        });
    }
]);

angular.module('badges').factory('UtilizatorService', ['$resource', function UtilizatorService($resource) {
    var base_url = '/users/api/1/utilizatori/';
    return $resource(base_url + ':id/', {
        id: '@id'
    }, {
        "get_current" : { method: "get", isArray: false, url: base_url + "get_current/" }
    })
}]);

angular.module("badges").controller("BadgeApproveController", ["$scope", "_", "BadgeService", function ($scope, _, BadgeService) {
    $scope.update_status = function update_status(id, new_status) {
        BadgeService.update_status({id: id, acceptat_status: new_status}, function (data) {
            console.log(data);
        })
    }
}]);

angular.module("badges").controller("BadgesController", ["$scope", "EvenimentService", "UtilizatorService", "_", function BadgesController($scope, EvenimentService, UtilizatorService, _) {
    $scope.page = 0;
    UtilizatorService.get_current().$promise.then(function (data) {
            $scope.user = data;
            $scope.page = 1;
            $scope.evenimente_count = 0;
            EvenimentService.query({page: $scope.page}, function (data) {
                $scope.evenimente_count = data.count;
                $scope.evenimente = data.results;
            });

        });

    $scope.load_more_badges = function load_more_badgrs() {
        if (!$scope.page || ($scope.page * 10 > $scope.evenimente_count)) {
            return;
        }

        if ($scope.loading === true) return;
        $scope.loading = true;

        $scope.page += 1
        EvenimentService.query({page: $scope.page}, function (data) {
            $scope.evenimente = _.union($scope.evenimente, data.results);
            $scope.loading = false;
        });

    }

    $scope.cercetasi_aici = function cercetasi_aici(event) {
        str = "";
        if ($scope.user_in_event(event)) {
            str = "Ai fost aici";
            if (event.badges.length > 1) {
                if (event.badges.length > 2) {
                    str += " împreună cu " + (event.badges.length - 1) + " alți cercetași"
                } else {
                    str += " împreună cu " + (event.badges.length - 1) + " alt cercetaș"
                }
            }
        } else {
            if (event.badges.length > 1) {
                str = event.badges.length + " cercetași au fost aici."
            }
        }
        return str;
    };

    $scope.user_in_event = function user_in_event(event) {
        return _.indexOf($scope.user.evenimente, event.id) >= 0
    }

}]);

angular.module("badges").controller("BadgeController", ["$scope", "BadgeService", "_", function BadgeController($scope, BadgeService, _) {

}])