const gulp = require('gulp');
const path = require('path');
const sourcemaps = require('gulp-sourcemaps');
const sass = require('gulp-dart-sass');
const autoprefixer = require('gulp-autoprefixer');
const gulpif = require('gulp-if');
const browserSync = require('browser-sync');
const fs = require('fs');


const _STATIC = path.resolve('static');
const PATHS = {
    src: {
      base: path.join(_STATIC, 'src'),
      other: path.join(_STATIC, 'src', 'other'),
      images: path.join(_STATIC, 'src', 'img'),
      scripts: path.join(_STATIC, 'src', 'js'),
      styles: path.join(_STATIC, 'src', 'scss'),
      stylesCss: path.join(_STATIC, 'src', 'css'),
    },
    dist: {
      base: path.join(_STATIC, 'dist'),
      other: path.join(_STATIC, 'dist', 'other'),
      images: path.join(_STATIC, 'dist', 'img'),
      scripts: path.join(_STATIC, 'dist', 'js'),
      styles: path.join(_STATIC, 'dist', 'css'),
    },
  };



function delete_dir(path){
    fs.rmSync(PATHS.dist.styles,{ recursive: true, force: true }, err => {
        if (err) {
          throw err
        }
        console.log(`${dir} is deleted!`)
      });
}

function css(prod = false){
  // console.log("handling scss");
  // delete_dir(PATHS.dist.styles)
  return gulp
  .src(path.join(PATHS.src.stylesCss, '**', '*.css'))
  .pipe(gulpif(!prod,sourcemaps.init()))
  .pipe(autoprefixer())
  .pipe(gulpif(!prod,sourcemaps.write()))
  .pipe(gulp.dest(PATHS.dist.styles))
  .pipe(browserSync.stream());
}

function scss(prod = false){
    // console.log("handling scss");
    // TODO : add check for same name css and scss files
    delete_dir(PATHS.dist.styles)
    css();
    return gulp
    .src(path.join(PATHS.src.styles, '**', '*.scss'))
    .pipe(gulpif(!prod,sourcemaps.init()))
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(gulpif(!prod,sourcemaps.write()))
    .pipe(gulp.dest(PATHS.dist.styles))
    .pipe(browserSync.stream());
}

function images() {
    // console.log("handling images");
    delete_dir(PATHS.dist.images)
    return gulp
      .src(path.join(PATHS.src.images, '**', '*'))
    //   .pipe(imagemin())
      .pipe(gulp.dest(PATHS.dist.images));
  }

function scripts(prod = false) {
    // console.log("handling scripts");
    delete_dir(PATHS.dist.scripts)
    return (
      gulp
        .src(path.join(PATHS.src.scripts, '**', '*.js'))
        // .pipe(gulpif(!prod, sourceMaps.init()))
        // .pipe(gulpif(prod, uglify()))
        // .pipe(gulpif(!prod, sourceMaps.write()))
        .pipe(gulp.dest(PATHS.dist.scripts))
    );
}

function other(prod = false) {
  // console.log("handling scripts");
  delete_dir(PATHS.dist.other)
  return (
    gulp
      .src(path.join(PATHS.src.other, '**', '*'))
      // .pipe(gulpif(!prod, sourceMaps.init()))
      // .pipe(gulpif(prod, uglify()))
      // .pipe(gulpif(!prod, sourceMaps.write()))
      .pipe(gulp.dest(PATHS.dist.other))
  );
}


function browserSyncServer(c) {
    browserSync.init({ proxy: 'localhost:8000' });
    c();
  }


function watchChanges(){
    // html
    gulp.watch(
      path.join(_STATIC, "..", '**', '*'))
      .on('all', browserSync.reload);

  gulp
    .watch(path.join(PATHS.src.images, '**', '*'))
    .on('all', gulp.series(images, browserSync.reload));

    gulp
    .watch(path.join(PATHS.src.other, '**', '*'))
    .on('all', gulp.series(other, browserSync.reload));

  gulp
    .watch(path.join(PATHS.src.scripts, '**', '*'))
    .on('all', gulp.series(scripts, browserSync.reload));

  gulp
    .watch(path.join(PATHS.src.stylesCss, '**', '*'))
    .on('all', gulp.series(scss, browserSync.reload));

  gulp
    .watch(path.join(PATHS.src.styles, '**', '*'))
    .on('all', gulp.series(scss,browserSync.reload));
}


gulp.task(
    'build',
    gulp.parallel(scss, images, scripts, other)
);
gulp.task(
    'watch', 
    gulp.series('build', browserSyncServer, watchChanges)
);




// ignore
function defaultTask(cb) {
    cb();
    console.log("default done");
}

exports.default = defaultTask;
