const memUsedStart = process.memoryUsage().heapUsed;
console.log('Test');
const memUsed = process.memoryUsage().heapUsed - memUsedStart;
console.log(memUsed / (1024 * 1024), 'Mb');
