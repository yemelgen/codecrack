#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifdef DEBUG
#  define DBG( format, ... ) printf( "DEBUG: "format, ## __VA_ARGS__ )
#else
#  define DBG( format, ...)
#endif

#define URIPATH_FILE_SIG "file"
#define URIPATH_TEXT_SIG "text"
#define URIPATH_HOSTNAME_MAX 1024

struct uripath {
	char *scheme;
	char *hostname;
	char *port;
	char *path;
	char *username;
	char *password;
	char *query;
	char *fragment;
};

/* these are for single-thread only, no malloc's */
struct uripath *uripath_load( const char *path );
void uripath_free( struct uripath *uri );
int uripath_magic( struct uripath *uri );
