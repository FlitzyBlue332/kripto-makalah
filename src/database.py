from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


engine = create_engine("sqlite:///public_keys.db")
s = Session(engine)

class Public_keys(SQLModel, table=True):
    '''
    isi database adalah:  
    nama:str
    public_keys:str
    '''
    id: Optional[int] = Field(default=None, primary_key=True)
    nama:str
    public_keys:str

# query
def getalldata():
    '''
    ambil semua data pada tabel train
    '''
    statement = select(Public_keys)
    datas = s.exec(statement).all()
    return datas

def getdatawithname(name):
    '''
    ambil data sesuai nama
    '''
    statement = select(Public_keys).where(Public_keys.nama == name)
    datas = s.exec(statement).all()
    return datas

def insertdata(nama, public_keys):
    '''
    insert data sesuai input
    '''
    sample = Public_keys(
        nama=nama,
        public_keys=public_keys
    )
    s.add(sample)
    s.commit()