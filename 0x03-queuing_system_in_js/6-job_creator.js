var kue = require('kue'); 

const queue = kue.createQueue();

const phone = '012-235-521';
const message = 'this message for you';
var job = queue.create('push_notification_code',
	{
		phoneNumber: phone,
		message: message,
}).save((err) => {

	if (!err) {
		console.log('Notification job created:', job.id);
}
});
	job.on('complete', (reply) => {
		console.log('Notification job completed');
});
	job.on('fail', (reply) => {
		console.log('Notification job failed');
});
