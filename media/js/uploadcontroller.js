uploadApp.controller('UploadController', function ($scope, $http, $resource){
	
	$http.get('/').success(function(data){
		$scope.leads = data;
	});

    $scope.leadUpload = {};

    $scope.submitData = function (lead)
    {
      var config = {
        params: {
          lead: lead
        }
      };

      $http.post("/", JSON.stringify(lead), config)
        .success(function (data, status, headers, config)
        {
          return $scope.leads.unshift(data);
        })
        .error(function (data, status, headers, config)
        {
          return $scope.errors = data;
        });
    };
});