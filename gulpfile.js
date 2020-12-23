'use strict';

const { src, dist, watch, parallel, series, task } = require('gulp');

function cleanDist(c) {
  console.log('cleaning');
  c();
}

function images(c) {
  console.log('images');
  c();
}

function sassCompile(c) {
  console.log('sassCompile');
  c();
}

function javaScript(c) {
  console.log('javaScript');
  c();
}

function others(c) {
  console.log('others');
  c();
}

function defaultGulp(r) {
  console.log('defaupt gulp');
  return series(cleanDist, parallel(javaScript, sassCompile, others, images));
}

task(
  'build',
  series(cleanDist, parallel(javaScript, sassCompile, others, images))
);
