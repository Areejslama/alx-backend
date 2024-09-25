var kue = require('kue')
var queue = kue.createQueue();

const blacklisted = [
    { phoneNumber: '4153518780' },
    { phoneNumber: '4153518781' }
];

const sendNotification = function(phoneNumber, message, job, done) {
    const total = 100;

    function black(p) {
        if (p === 0 || p === (total / 2)) {
            job.progress(p, total);
            if (p === total / 2) {
                console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
            }
        }
	    if (blacklisted.includes(job.data.phoneNumber)) {
		    return done(new Error(`Phone number ${job.data.phoneNumber} is blacklisted`));
        }

        if (p === total) {
            return done();
        }

         return black(p + 1);
    }
	

    black(0);
};

queue.process('push_notification_code_2', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
