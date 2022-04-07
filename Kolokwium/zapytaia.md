http://localhost:${port}/findByNameFirstNameDomain
zapytanie get
znalezienie wszystkich rekorodow po nastepujacych polach podanych w body:
{
    first_name,
    second_name,
    domain,
}
http://localhost:${port}/
zapytanie post
dodanie uzytkownika. posiada walidacje okreslona w pliku User.js
http://localhost:${port}/domaincost/:domain
zapytanie get
zwraca koszt domeny podanej w parametrze :domain
http://localhost:${port}//:idUser
zapytanie delete
usuwa objekt o id podanym w :idUser