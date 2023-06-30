#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/*
 * This program demonstrates the creation of zombie processes.
 * It creates 5 child processes that immediately exit, becoming zombies.
 * The parent process prints the PID of each zombie process created.
 */

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    int i;
    pid_t child_pid;

    // Create 5 child processes that immediately exit
    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid > 0) // Parent process
        {
            printf("Zombie process created, PID: %d\n", child_pid);
            sleep(1);
        }
        else if (child_pid == 0) // Child process
        {
            exit(0);
        }
        else // Forking error
        {
            perror("Forking error");
            exit(1);
        }
    }

    infinite_while();

    return (0);
}
