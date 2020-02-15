int increment(int nb)
{
    return (nb + 42);
}

int main(void)
{
    int nb = 1;
    int nb_2 = 4;

    if (nb_2 + nb == 5)
        nb_2 = increment(nb_2);
    else
        nb += 1;
    return (nb_2 + nb);
}
