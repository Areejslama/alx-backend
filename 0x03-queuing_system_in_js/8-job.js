var kue = require('kue');
var queue = kue.createQueue();

const createPushNotificationsJobs = function(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    for (let job of jobs) {
        job = queue.create('push_notification_code_3', job)
            .save((err) => {
                if (!err) {
                    console.log('Notification job created:', job.id);
                } else {
                    console.log('Error creating job:', err);
                }
            });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        });

        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} is ${progress}% complete`);
        });
    }
};

module.exports =  createPushNotificationsJobs;
