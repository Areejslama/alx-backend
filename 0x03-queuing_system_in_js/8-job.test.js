import { createPushNotificationsJobs } from '8-job';
var kue = require('kue');
var queue = kue.createQueue();

describe('test queue', function() {
	 before(function () {
		 queue.testMode.enter();
  });
	 afterEach(function () {
		 queue.testMode.clear();
 });
