#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "gd.h"
#include "ugm_defines.h"
#include "ugm_typedefs.h"
#include "grid_obj.h"

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input.gif> <output.gif>\n", argv[0]);
        return 1;
    }

    char *in_filename = argv[1];
    char *out_filename = argv[2];

    gdImagePtr im;
    FILE *in;

    in = fopen(in_filename, "rb");
    if (!in) {
        fprintf(stderr, "Error opening input file %s\n", in_filename);
        return 1;
    }

    im = gdImageCreateFromGif(in);
    fclose(in);

    if (!im) {
        fprintf(stderr, "Error reading GIF from %s\n", in_filename);
        return 1;
    }

    for (int y = 0; y < im->sy; y++) {
        for (int x = 0; x < im->sx; x++) {
            int pixel = gdImageGetPixel(im, x, y);
            if (pixel != 0 && pixel != 100) {
                gdImageSetPixel(im, x, y, 0);
            }
        }
    }

    FILE *out = fopen(out_filename, "wb");
    if (!out) {
        fprintf(stderr, "Error opening output file %s\n", out_filename);
        gdImageDestroy(im);
        return 1;
    }

    gdImageGif(im, out);
    fclose(out);

    gdImageDestroy(im);

    return 0;
}