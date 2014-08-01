var uploadApp = angular.module('UploadApp', ['ngResource']);

uploadApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);
