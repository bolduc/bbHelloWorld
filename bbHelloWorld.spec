/*
A KBase module: bbHelloWorld
*/

module bbHelloWorld {
    /*
        Insert your typespec information here.
    */

typedef structure {
        string phrase;
    } InParams;

typedef structure {
        string phrase;
    } OutParams;

funcdef printhelloworld(InParams params)
        returns (OutParams) authentication required;

};
