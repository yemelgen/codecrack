#include "uripath.h"

static void parse_path(struct uripath *uri, char *start)
{
	char *end = start;

	/* reading path */
	while (*end != '#' && *end != '?' && *end != '\0') end++;
	if (end - start > 0) {
		uri->path = strndup(start, end - start);
		DBG("uri->path='%s'\n", uri->path);
	}
	start = end;

	/* reading query */
	if (*start == '?') {
		end = ++start;
		while (*end != '#' && *end != '\0') end++;
		if (end - start > 0) {
			uri->query = strndup(start, end - start);
			DBG("uri->query='%s'\n", uri->query);
		}
		start = end;
	}

	/* reading fragment */
	if (*start == '#') {
		end = ++start;
		while (*end != '\0') end++;
		if (end - start > 0) {
			uri->fragment = strndup(start, end - start);
			DBG("uri->fragment='%s'\n", uri->fragment);
		}
		start = end;
	}

}

struct uripath *uripath_load(const char *uristring)
{
	char *start, *end;
	int i;
	int userflag, ipv6flag;
	struct uripath *uri = malloc(sizeof(struct uripath));

	uri->scheme = NULL;
	uri->hostname = NULL;
	uri->port = NULL;
	uri->path = NULL;
	uri->username = NULL;
	uri->password = NULL;
	uri->query = NULL;
	uri->fragment = NULL;

	start = (char*)uristring;

	/* check for null */
	if (!uristring || !strlen(uristring)) return 0;

	/* look for scheme */
	end = strchr(start, ':');

	/* scheme was not found */
	if ( end == NULL ) {
		if ( access( start, F_OK ) != -1 ) {
			uri->scheme = strdup( URIPATH_FILE_SIG );
			/* extract path, query, and fragment */
			parse_path(uri, start);
			DBG("uri->scheme='%s'\n", uri->scheme );
			DBG("uri->path='%s'\n", uri->path );
			return uri;
		} else {
			uri->scheme = strdup( URIPATH_TEXT_SIG );
			/* extract path, query, and fragment */
			parse_path(uri, start);
			DBG("uri->scheme='%s'\n", uri->scheme );
			DBG("uri->path='%s'\n", uri->path );
			return uri;
		}
	}

	/* scheme was found */
	uri->scheme = strndup( start, end - start);
	DBG("uri->scheme='%s'\n", uri->scheme );

	/* skip the '://' */
	start = ++end;
	for ( i = 0; i < 2 && *start == '/'; i++ ) start++;

	/* check for user and password */
	end = start;
	userflag = 0;
	while (*end != '\0') {
		if (*end == '@') {
			userflag = 1;
			break;
		} else if (*end == '/') {
			userflag = 0;
			break;
		}
		end++;
	}

	/* read user and password */
	end = start;
	if (userflag) {
		while (*end != ':' && *end != '@' & *end != '\0') end++;
		if (end - start > 0) {
			uri->username = strndup(start, end - start);
			DBG("uri->username='%s'\n", uri->username);
		}
		start = end;
		if (*start == ':') {
			end = ++start;
			while (*end !='@' && *end != '\0') end++;
			if ( end - start > 0 ) {
				uri->password = strndup(start, end - start);
				DBG("uri->password='%s'\n", uri->password);
			}
			start = end;
		}
		start++;
	}

	/* check for ipv6 */
	ipv6flag = *start == '[' ? 1 : 0;

	/* read hostname */
	end = start;
	while ( *end != '\0' ) {
		if ( ipv6flag && *end == ']' ) {
			end++;
			break;
		} else if ( !ipv6flag && ( *end == ':' || *end == '/' ) )
			break;
		end++;
	}
	if ( end - start > 0 ) {
		uri->hostname = strndup( start, end - start );
		DBG("uri->hostname='%s'\n", uri->hostname );
	} 
	start = end;

	/* read port */
	if (*start == ':') {
		end = ++start;
		while (*end != '/' && *end != '\0') end++;
		if (end - start > 0) {
			uri->port = strndup(start, end - start);
			DBG("uri->port='%s'\n", uri->port);
		}
		start = end;
	}

	/* read path, query, and fragment */
	parse_path(uri, start);;
	return uri;
}

void uripath_free(struct uripath *uri)
{
	if (NULL == uri) return;

	if (uri->scheme != NULL)
		free( uri->scheme );
	if (uri->hostname != NULL)
		free( uri->hostname );
	if (uri->port != NULL)
		free(uri->port);
	if (uri->path != NULL)
		free(uri->path);
	if (uri->username != NULL)
		free(uri->username);
	if (uri->password != NULL)
		free(uri->password);
	if (uri->query != NULL)
		free(uri->query);
	if (uri->fragment != NULL)
		free(uri->fragment);
	free(uri);
}


#ifdef TEST_URIPATH
int main( int argc, char *argv[] )
{
	struct uripath *uri;

	uri = uripath_load( argv[1] );
	if ( uri ) {
		printf("scheme: %s\n", uri->scheme );
		printf("username: %s\n", uri->username );
		printf("password: %s\n", uri->password );
		printf("hostname: %s\n", uri->hostname );
		printf("port: %s\n", uri->port );
		printf("path: %s\n", uri->path );
		printf("query: %s\n", uri->query );
		printf("fragment: %s\n", uri->fragment );
	}
	uripath_free( uri );

}
#endif
