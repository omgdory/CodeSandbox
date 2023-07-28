#include <iostream>
#include <vector>

class MatrixException : public std::exception {
public:
    std::string what() {
        return "Matrix used improperly";
    }
};

class RowNotEqualColumnException : public MatrixException {
public:
    std::string what() {
        return "Row size of first matrix must be equal to column size of second matrix.";
    }
};

class AssignmentOperatorException : public MatrixException {
public:
    std::string what() {
        return "Matrix assigned improperly.";
    }
};

class Matrix {
    int rowAmount;
    int colAmount;
    std::vector< std::vector<float> > mtx;

public:
    Matrix() {
        rowAmount = 0;
        colAmount = 0;
        mtx = {};
    }

    Matrix(int rowAmount, int colAmount) {
        this->rowAmount = rowAmount;
        this->colAmount = colAmount;
        for(int row=0; row<rowAmount; row++) {
            mtx.push_back({});
            for(int col=0; col<colAmount; col++) {
                mtx[row].push_back(0);
            }
        }
    }

    std::vector<float> operator[](int i) {
        return mtx[i];
    }

    void operator=(const Matrix &toCopy) {
        rowAmount = toCopy.rowAmount;
        colAmount = toCopy.colAmount;
        mtx = toCopy.mtx;
    }

    void operator=(const std::vector< std::vector<float> > &toCopy) {
        rowAmount = toCopy.size();
        if(rowAmount = 0)
            colAmount = 0;
        else
            colAmount = toCopy[0].size();
        mtx = toCopy;
    }
    
    static Matrix matrixMultiply(Matrix m1, Matrix m2) {
        if(m1.rowAmount != m2.colAmount) {
            throw RowNotEqualColumnException();
            return Matrix();
        }

        Matrix result;
        
        // multiply

        return result;
    }
};

int main() {
    
    return 0;
}
