var gutil = requir('gulp-util');

exports.path = {
    src  :  'blogalot/frontend/static',
    tmp  :  '.tmp'
}

exports.wiredep = {
    directory: 'bower_components'
};


exports.errorHandler = function (title)
{
    'use strict';

    return function (err)
    {
	gutil.log(gutil.colors.red('[' + title ']'), err.toString());
	this.emit('end');
    };
};
