// -- I didn't know a thing about nodejs when I started doing this
// -- so...
// -- I can't really explain how everything here works
// -- most of these were StackOverflowed from different sources (a lot of them)

// -- I have a certain level of understanding, cause 
// -- I learned some about Stream, Buffers, request, etc. in nodejs
// -- while doing that, but still can't give a proper explanation

// -- there is not much of a code, so it will probably be self-explanatory

const fs = require('fs');
const request = require('request');
const archiver = require('archiver');

const rawdata = fs.readFileSync('urls.json');
const urls = JSON.parse(rawdata);

const output = fs.createWriteStream(__dirname + '/pics.zip');
const archive = archiver('zip', {
        zlib: {level: 9}
});

output.on('close', () => {
        console.log('Archive size: ', archive.pointer() / (1024 * 1024), 'Mb');
        console.log('Done');
});

archive.pipe(output);

// -- it cost me about 6 hours of try/fail sequeunces and googling
// -- to make next 3 lines work
// -- everything else I did in less than 2 hours

urls.map((u, index) => {
        archive.append(request(u), { name: 'img' + index + '.jpg' });
});

archive.finalize();

const memUsed = process.memoryUsage().heapUsed;
console.log('Memory used: ', memUsed / (1024 * 1024), 'Mb');
