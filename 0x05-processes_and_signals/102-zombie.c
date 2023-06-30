#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * This function runs an infinite while loop using the sleep function.
 * It is used to keep the program running after creating the zombie processes.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * This function creates five child processes using fork.
 * The parent process prints the PID of the zombie processes and continues.
 * The child processes exit immediately, becoming zombies.
 * The program then enters an infinite while loop to keep running.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;
	int zombie_count;

	/* Create five zombie processes */
	for (zombie_count = 0; zombie_count < 5; zombie_count++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else if (child_pid == 0)
		{
			/* Child process */
			exit(0);
		}
		else
		{
			/* Fork failed */
			perror("fork");
			exit(EXIT_FAILURE);
		}
	}

	/* Keep the program running */
	infinite_while();

	return (0);
}
