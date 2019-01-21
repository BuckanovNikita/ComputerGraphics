#include "loadbmp.h"

GLuint TexId;

char strFile[] = "wallpaper.bmp";
IMAGE img;
glPixelStorei(GL_UNPACK_ALIGNMENT, 1 );
glGenTextures(1,&TexId );
if( !LoadBMP( strFile , &img )) {
	return; // error
}
glBindTexture(GL_TEXTURE_2D, TexId );
gluBuild2DMipmaps(GL_TEXTURE_2D,3 ,	img.width, img.height, GL_RGB,GL_UNSIGNED_BYTE, img.data);

glEnable(GL_TEXTURE_2D);

glTexCoord2f(..., ...); 
glVertex3f(..., ..., ...);

